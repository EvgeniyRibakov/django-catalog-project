# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForms, ProductModeratorForms
from catalog.models import Product
from catalog.services import get_products_by_category
from django.core.cache import cache


# Главная страница
class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


# Страница контактов
class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        cache_key = 'product_list_all'
        products = cache.get(cache_key)
        if not products:
            products = super().get_queryset()
            cache.set(cache_key, products, timeout=60*15)  # Кэш на 15 минут
        return products


# Детали продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


# Создание нового продукта
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForms
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


# Обновление продукта
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForms
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        # Получаем объект продукта
        obj = super().get_object(queryset)
        # Проверяем, является ли текущий пользователь владельцем
        if obj.owner != self.request.user:
            # Если не владелец и нет специальных разрешений, запрещаем доступ
            if not (self.request.user.has_perm("catalog.can_edit_product") and
                    self.request.user.has_perm("catalog.can_edit_description")):
                raise PermissionDenied("Вы не можете редактировать этот продукт.")
        return obj

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForms
        if user.has_perm("catalog.can_edit_product") and user.has_perm("catalog.can_edit_description"):
            return ProductModeratorForms
        raise PermissionDenied("У вас нет прав для редактирования этого продукта.")


# Удаление продукта
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        # Получаем объект продукта
        obj = super().get_object(queryset)
        # Проверяем, является ли текущий пользователь владельцем
        if obj.owner != self.request.user:
            raise PermissionDenied("Вы не можете удалить этот продукт.")
        return obj


class ProductByCategoryListView(ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_name = self.kwargs['category']
        return get_products_by_category(category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context

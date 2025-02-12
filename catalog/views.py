# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForms  # Исправлена ошибка в импорте
from catalog.models import Product


# Главная страница
class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


# Страница контактов
class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


# Просмотр списка продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


# Детали продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


# Создание нового продукта
class ProductCreateView(CreateView, LoginRequiredMixin):
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
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForms
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_list')


# Удаление продукта
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
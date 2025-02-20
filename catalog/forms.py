from django import forms
from .models import Product

# Список запрещенных слов
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
    'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForms, self).__init__(*args, **kwargs)
        # Применение классов к каждому полю формы
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    # Валидация названия и описания на запрещенные слова
    def clean_name(self):
        name = self.cleaned_data.get('name').lower()  # Приводим к нижнему регистру
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError(f'Название не может содержать слово "{word}".')
        return self.cleaned_data.get('name')

    def clean_description(self):
        description = self.cleaned_data.get('description').lower()  # Приводим к нижнему регистру
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError(f'Описание не может содержать слово "{word}".')
        return self.cleaned_data.get('description')

    def clean_price(self):
        price = self.cleaned_data.get('price')

        # Проверяем, что цена не отрицательная
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")

        return price


class ProductModeratorForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'category', 'category', 'price']
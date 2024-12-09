from django.core.exceptions import ValidationError
from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "дёшево", "бесплатно", "обман",
                           "полиция",
                           "радар"]
        name = self.cleaned_data.get('name')
        if name.lower() in forbidden_words:
            raise ValidationError('Название содержит запрещенное слово')
        return name

    def clean_description(self):
        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "дёшево", "бесплатно", "обман",
                           "полиция","радар"]
        description = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError('Описание содержит запрещенное слово')

        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')

        return price

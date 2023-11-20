from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'price',
            # 'create_date',
            'preview_image'
        ]


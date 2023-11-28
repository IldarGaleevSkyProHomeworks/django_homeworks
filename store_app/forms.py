from django import forms

from store_app.models import Product


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


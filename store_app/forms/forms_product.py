from django import forms

from store_app.models import Product
from store_app.utils import find_deprecated_subjects


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

    def clean_name(self):
        field = self.cleaned_data.get('name')

        deprecated_subjects = find_deprecated_subjects(field)
        if deprecated_subjects:
            raise forms.ValidationError('Имя содержит слова из недопустимых тематик: '
                                        f'{", ".join(deprecated_subjects)}')
        return field

    def clean_description(self):
        field = self.cleaned_data.get('description')
        deprecated_subjects = find_deprecated_subjects(field)
        if deprecated_subjects:
            raise forms.ValidationError('Описание содержит слова из недопустимых тематик: '
                                        f'{", ".join(deprecated_subjects)}')
        return field

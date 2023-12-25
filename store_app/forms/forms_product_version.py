from django import forms
from django.forms import inlineformset_factory

from store_app.models import ProductVersion, Product
from store_app.utils import find_deprecated_subjects


class ProductVersionForm(forms.ModelForm):
    class Meta:
        model = ProductVersion
        fields = [
            'version_name',
            'version_number',
            'is_latest',
            'product'
        ]

    def clean_version_name(self):
        field = self.cleaned_data.get('version_name')
        deprecated_subjects = find_deprecated_subjects(field)
        if deprecated_subjects:
            raise forms.ValidationError('Название версии содержит слова из недопустимых тематик: '
                                        f'{", ".join(deprecated_subjects)}')
        return field


ProductVersionFormset = inlineformset_factory(
    Product,
    ProductVersion,
    form=ProductVersionForm,
    extra=1
)

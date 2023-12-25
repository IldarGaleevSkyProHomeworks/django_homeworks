from django import forms
from django.core.exceptions import ValidationError
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


ProductVersionFormsetBase = inlineformset_factory(
    Product,
    ProductVersion,
    form=ProductVersionForm,
    extra=1
)


class ProductVersionFormset(ProductVersionFormsetBase):
    def clean(self):
        version_forms = self.forms
        is_latest_count = len([1 for f in version_forms if f.instance.is_latest])
        if is_latest_count > 1:
            raise ValidationError('Может быть только одна активная версия!')
        super().clean()

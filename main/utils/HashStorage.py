import hashlib
import os.path
from django.core.files import File
from django.core.files.utils import validate_file_name
from django.core.files.storage import FileSystemStorage


class HashStorage(FileSystemStorage):

    def save(self, name, content, max_length=None):
        if name is None:
            name = content.name

        if not hasattr(content, "chunks"):
            content = File(content, name)

        if not self.exists(name):
            name = self._save(name, content)

        validate_file_name(name, allow_relative_path=True)
        return name


def product_preview_images(instance, filename):
    instance.preview_image.open()
    context = instance.preview_image.read()
    _, ext = os.path.splitext(filename)

    file_path = 'product_preview_images/' + hashlib.md5(context).hexdigest() + ext

    return file_path
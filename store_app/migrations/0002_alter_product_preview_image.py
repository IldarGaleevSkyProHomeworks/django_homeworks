# Generated by Django 4.2.7 on 2023-11-28 12:47

from django.db import migrations, models

from utils.hash_storage import HashStorage, product_preview_images


class Migration(migrations.Migration):

    dependencies = [
        ("store_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="preview_image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=HashStorage(),
                upload_to=product_preview_images,
                verbose_name="изображение",
            ),
        ),
    ]

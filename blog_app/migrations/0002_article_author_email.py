# Generated by Django 4.2.7 on 2023-11-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author_email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="email автора"
            ),
        ),
    ]
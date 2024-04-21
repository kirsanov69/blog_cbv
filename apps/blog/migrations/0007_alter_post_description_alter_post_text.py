# Generated by Django 5.0.3 on 2024-04-19 05:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=500, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Полный текст записи'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-26 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0006_rename_mymodel_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Synopsis',
            new_name='synopsis',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Year',
            new_name='year',
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0010_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Horror', 'HORROR'), ('Romance', 'ROMANCE'), ('Fantasy', 'FANTASY'), ('Humour and satire', 'HUMOUR AND SATIRE'), ('Education', 'EDUCATION'), ('Other', 'OTHER')], default='Other', max_length=20),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_rename_a_decimal_mymodel_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='Author',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

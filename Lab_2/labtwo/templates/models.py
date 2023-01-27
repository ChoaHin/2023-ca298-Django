from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.CharField(max_length=20) # charfields have to have a max length
    price = models.DecimalField(max_digits=5, decimal_places=2) # number from 0.0-999.99S
    title = models.CharField(max_length=20, null=True)
    category_choice = [
        ('Horror','HORROR'),
        ('Romance','ROMANCE'),
        ('Fantasy','FANTASY'),
        ('Humour and satire','HUMOUR AND SATIRE'),
        ('Education','EDUCATION'),
        ('Other','OTHER') ]
    category = models.CharField(choices=category_choice, default='Other', max_length=20)
    synopsis = models.TextField()

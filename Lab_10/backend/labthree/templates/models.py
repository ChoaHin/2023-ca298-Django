from django.db import models
import datetime

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    genre = models.CharField(max_length=20)
    # YEAR_CHOICES = [(r,r) for r in range(0000, datetime.date.today().year+1)]
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    number_in_inventory = models.IntegerField()

class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)

class Record(models.Model):
    id = models.AutoField(primary_key = True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=7))
    is_returned = models.BooleanField()

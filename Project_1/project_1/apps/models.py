from django.db import models
from django import forms
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

# Create your models here.
#Customer model
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Full name', max_length=1024)
    address1 = models.CharField('Address line 1', max_length=1024, null=True)
    address2 = models.CharField('Address line 2', max_length=1024, blank=True)
    cc_number = CardNumberField('Card number')
    cc_expiry = CardExpiryField('Card expiry')
    cc_code = SecurityCodeField('Card security code')

#Pizza model
class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Sauce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):  
        return self.name

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    owned_by = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    # - size - small, medium, large
    # - crust size - normal, thin, thick, gluten free
    # - sauce - tomato, bbq
    # - cheese - mozzarella, vegan, low fat
    # - topping - pepperoni, chicken, ham, pineapple, pepper, mushroom, onion
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust_choices = [
    #('value','display')
    ('Normal', 'Normal'),
    ('Thin','Thin'),
    ('Thick','Thick'),
    ('Gluten free','Gluten Free')
    ]
    crust_size = models.CharField(choices=crust_choices, max_length=20)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    topping = models.CharField(max_length=1000)
    def __str__(self):
        return self.size.name + " " + self.crust_size + " " + self.sauce.name + " " + self.cheese.name + " " + self.topping
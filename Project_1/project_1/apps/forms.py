#imports for forms.py 
from django import forms
from .models import * # import all of your models
from django.core.exceptions import ValidationError
   
class PizzaForm(forms.ModelForm):
    topping_choices = [
    ('pepperoni', 'PEPPERPONI'),
    ('chicken', 'CHICKEN'),
    ('ham','HAM'),
    ('pineapple','PINEAPPLE'),
    ('pepper','PEPPER'),
    ('mushroom','MUSHROOM'),
    ('onion','ONION'),
]

    topping = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=topping_choices,
        required=False
    )

    class Meta:
        model = Pizza
        fields = ['size', 'crust_size', 'sauce', 'cheese', 'topping']

    widgets = {
        'size': forms.Select(attrs={'class': 'form-control'}),
        'crust_size': forms.Select(attrs={'class': 'form-control'}),
        'sauce': forms.Select(attrs={'class': 'form-control'}),
        'cheese': forms.Select(attrs={'class': 'form-control'}),
        'topping': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
    }


class DetailForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'address1', 'address2', 'cc_number', 'cc_expiry', 'cc_code']
    
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control',}),
        'address1': forms.TextInput(attrs={'class': 'form-control'}),
        'address2': forms.TextInput(attrs={'class': 'form-control'}),
        'cc_number': forms.TextInput(attrs={'class': 'form-control'}),
        'cc_expiry': forms.TextInput(attrs={'class': 'form-control'}),
        'cc_code': forms.TextInput(attrs={'class': 'form-control'}),
    }
# serializers.py created inside your app folder
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ['id','first_name','last_name']
		
class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['title', 'author', 'genre', 'year', 'number_in_inventory']

class RecordSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Record
		fields = ['id', 'book', 'customer', 'due_date', 'is_returned']

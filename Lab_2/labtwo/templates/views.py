from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

def base(request):
    return render(request, 'base.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, 'single_book.html', {'book':single_book})

def view_specific_year(request, year):
    specific_year = Book.objects.filter(year = year)
    return render(request, 'all_books.html', {'books':specific_year})

def view_specific_category(request, category):
    specific_category = Book.objects.filter(category__iexact=category)
    return render(request, 'all_books.html', {'books':specific_category})

def view_category_year(request, category, year):
    specific_category_year = Book.objects.filter(category__iexact=category, year = year)
    return render(request,'all_books.html', {'books':specific_category_year}  )

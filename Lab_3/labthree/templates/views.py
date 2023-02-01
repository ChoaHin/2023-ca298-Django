from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, 'single_book.html', {'book':single_book})

def view_specific_year(request, year):
    specific_year = Book.objects.filter(year = year)
    return render(request, 'all_books.html', {'books':specific_year})

def view_specific_genre(request, genre):
    specific_genre = Book.objects.filter(genre__iexact=genre)
    return render(request, 'all_books.html', {'books':specific_genre})

def view_genre_year(request, genre, year):
    specific_genre_year = Book.objects.filter(genre__iexact=genre, year = year)
    return render(request,'all_books.html', {'books':specific_genre_year}  )

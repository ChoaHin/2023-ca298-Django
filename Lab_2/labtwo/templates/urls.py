from .views import *
from django.urls import path

urlpatterns = [
   path('', base, name="base"),
   path('books', view_all_books, name="all_books"),
   path('books/<int:bookid>', view_single_book, name='single_book'),
   path('books/year/<int:year>', view_specific_year, name='all_books'),
   path('books/category/<str:category>', view_specific_category, name='all_books'),
   path('books/category/<str:category>/year/<int:year>',view_category_year, name="all_books"),
]
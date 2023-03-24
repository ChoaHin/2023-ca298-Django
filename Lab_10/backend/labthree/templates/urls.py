from .views import *
from django.urls import path, include
from rest_framework import routers
from . import views

# create and define our router 
router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'book',views.BookViewSet)
router.register(r'record', views.RecordViewSet)

urlpatterns = [
   path('', index, name="index"),
   path('books', view_all_books, name="all_books"),
   path('books/<int:bookid>', view_single_book, name='single_book'),
   path('books/year/<int:year>', view_specific_year, name='all_books'),
   path('books/genre/<str:genre>', view_specific_genre, name='all_books'),
   path('books/genre/<str:genre>/year/<int:year>',view_genre_year, name="all_books"),
   path('customer/<int:custid>',show_customer, name="customer"),
   path('add', api_add, name='api_add'),
   path('subtract', api_subtract, name='api_subtract'),
   path('divide', api_divide, name='api_divide'),
   path('multiply', api_multiply, name='api_multiply'),
   path('exponential', api_exponential, name='api_exponential'),
   path('api-auth/', include('rest_framework.urls')),
   path('api',include(router.urls),)    
]
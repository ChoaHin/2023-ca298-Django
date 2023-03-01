from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('createpizza',views.create_pizza, name='create_pizza'),
    path('detail/<int:pizzaid>',views.detail, name='detail'),
    path('final/<int:custid>',views.final, name='final')
]
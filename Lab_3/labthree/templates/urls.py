from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('test', include('your_app_name.urls')),
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
]
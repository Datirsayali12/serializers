"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_data/',views.student_list_create,name="get_data"),
    path('get_student/<int:pk>',views.user_list,name="get_data"),
    path('save_data/<int:pk>',views.data_save,name="get_data"),
    path('get_books/',views.get_books,name="get_data"),
    path('get_book/<int:pk>',views.get_book,name="get_data"),



]

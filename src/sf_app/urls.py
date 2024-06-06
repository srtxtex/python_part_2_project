"""
Модуль выполняет диспетчеризацию и перенаправление запросов
в указанную функцию обработчик
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('faqs', views.faqs, name='faqs'),
    path('abouts', views.abouts, name='abouts'),
    path('admin', admin.site.urls),
]

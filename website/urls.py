from os import name
from website.views import delete, update
from django.contrib import admin
from django.core.exceptions import ViewDoesNotExist
from django.urls import path
from website import views

app_name = 'website'
urlpatterns = [
    # List of all Books present in database
    path('', views.index, name='index'),

    # Book detail url
    path('book/<int:book_id>/', views.book_detail, name='detail'),
    # Adding the book urls 
    path('add/', views.add_book, name='add_book'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

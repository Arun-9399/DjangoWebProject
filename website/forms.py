# django form for edit, delete, or save and update functionality
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'desc', 'price', 'book_image']

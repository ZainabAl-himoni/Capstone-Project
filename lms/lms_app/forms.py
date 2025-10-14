from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'photo_book', 'pages', 'price', 'rental_price_day', 'status', 'category', 'rating', 'description']

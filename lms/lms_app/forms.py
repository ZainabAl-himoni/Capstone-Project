from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    rating = forms.IntegerField(
        required=False,  
        min_value=0,     
        max_value=5,     
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter rating (1-5)',  
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'photo_book', 'pages', 'price',
                  'rental_price_day', 'status', 'category', 'rating', 'description']

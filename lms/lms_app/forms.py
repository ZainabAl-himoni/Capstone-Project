from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    rating = forms.DecimalField(
        required=False,
        min_value=0,    
        max_value=5,      
        decimal_places=1, 
        max_digits=3,     
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter rating (0-5, e.g. 4.5)',
            'step': '0.1',  
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'photo_book', 'pages', 'price',
                  'rental_price_day', 'status', 'category', 'rating', 'description']


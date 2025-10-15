from django import forms
from .models import Book, Comment  

class BookForm(forms.ModelForm):
    rating = forms.DecimalField(
        required=False,
        min_value=0,    
        max_value=5,      
        decimal_places=1, 
        max_digits=3,     
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter rating ( 0 - 5)',
            'step': '0.1',  
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'photo_book', 'pages', 'price',
                  'rental_price_day', 'status', 'category', 'rating', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  
        fields = ['name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add your comment here...', 'rows': 3}),
            'name': forms.TextInput(attrs={'placeholder': 'Your name (optional)'}),
        }

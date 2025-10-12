from django.shortcuts import render
from .models import Book, Category

def home(request):
    books = Book.objects.all()

    
    categories = Category.objects.prefetch_related('book_set').all()

    
    chart_labels = [cat.name for cat in categories]
    chart_data = [cat.book_set.count() for cat in categories]

    context = {
        'books': books,
        'categories': categories,
        'chart_labels': chart_labels,
        'chart_data': chart_data
    }
    return render(request, 'home.html', context)

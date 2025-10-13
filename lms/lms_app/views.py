from django.shortcuts import render, redirect
from .models import Book, Category


def home(request):
    
    books = Book.objects.all()

    categories = Category.objects.prefetch_related('book_set').all()

    chart_labels = [category.name for category in categories]
    chart_data = [category.book_set.count() for category in categories]

    context = {
        'books': books,
        'categories': categories,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }

    return render(request, 'home.html', context)


def about(request):
    
    return render(request, 'about.html')


def admin_redirect(request):
    
    return redirect('/admin/')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book, Category
from django.contrib.auth import logout
from .models import Book
from django.db.models import ProtectedError
from .forms import BookForm  
from django.db.models import Q

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

def user_logout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'about.html')

def admin_redirect(request):
    return redirect('/admin/')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
    
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    
    return render(request, 'register.html')

from .forms import BookForm  

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully ✅")
            return redirect('home')
    else:
        form = BookForm(instance=book)

    return render(request, 'books/add_book.html', {
        'form': form,
        'is_edit': True,
        'book': book
    })



def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book.delete()
        return redirect('home')
    return render(request, 'books/delete_book.html', {'book': book})


def add_category(request):
    next_url = request.GET.get('next', '/home/')
    # أضف anchor للـ Category
    if not next_url.endswith('#id_category'):
        if '#' in next_url:
            next_url = next_url.split('#')[0] + '#id_category'
        else:
            next_url += '#id_category'

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            if Category.objects.filter(name__iexact=name).exists():
                messages.error(request, "Category already exists.")
            else:
                Category.objects.create(name=name)
                messages.success(request, "Category added successfully!✅")
                return redirect(next_url)  # إعادة التوجيه مع anchor
        else:
            messages.error(request, "Please enter a category name.")
    return render(request, 'books/add_category.html')

def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            category.name = name
            category.save()
            messages.success(request, "Category updated successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please enter a category name.")
    return render(request, 'books/edit_category.html', {'category': category})

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted successfully!")
        return redirect('home')
    messages.error(request, "Invalid request method.")
    return redirect('home')



def manage_categories(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        if 'save_changes' in request.POST:
            # Save name changes
            for category in categories:
                new_name = request.POST.get(f'name_{category.id}')
                if new_name and new_name != category.name:
                    category.name = new_name
                    category.save()
            messages.success(request, "Changes saved successfully ✅")

        elif 'delete_selected' in request.POST:
            ids_to_delete = request.POST.getlist('delete_ids')
            if ids_to_delete:
                try:
                    Category.objects.filter(id__in=ids_to_delete).delete()
                    messages.success(request, "Selected categories deleted successfully 🗑️")
                except ProtectedError:
                    # Cannot delete categories linked to books
                    messages.error(request, "Cannot delete some categories because they are linked to existing books 📚")

        return redirect('manage_categories')

    return render(request, 'books/manage_categories.html', {'categories': categories})


def delete_categories(request):
    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('delete_ids')
        if ids_to_delete:
            Category.objects.filter(id__in=ids_to_delete).delete()
    return redirect('manage_categories')


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})




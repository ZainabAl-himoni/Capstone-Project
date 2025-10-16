from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book, Category
from django.contrib.auth import logout
from .forms import BookForm  
from django.db.models import ProtectedError
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import BookForm, CommentForm 
from django.db import models
from .models import Book, Category, Comment
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.http import JsonResponse

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


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    my_books = request.session.get('my_books', [])

    if not request.user.is_superuser and book.id not in my_books:
        return redirect('home')  

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    return render(request, 'books/add_book.html', {
        'form': form,
        'is_edit': True,
        'book': book
    })




@login_required
def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return redirect('home')  

    my_books = request.session.get('my_books', [])

    
    if not request.user.is_superuser and book.id not in my_books:
        return redirect('home')  

    if request.method == "POST":
        book.delete()
        if not request.user.is_superuser and book.id in my_books:
            my_books.remove(book.id)
            request.session['my_books'] = my_books
        return redirect('home')

    return render(request, 'books/delete_book.html', {'book': book})




@login_required
def add_category(request):
    back_url = '/home/'
    next_url = request.GET.get('next')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        if name:
            if Category.objects.filter(name__iexact=name).exists():
                messages.error(request, "Category already exists.")
            else:
                Category.objects.create(name=name)
                messages.success(request, "Category added successfully! ✅")

                if next_url:
                    return redirect(next_url)
                
                return redirect('manage_categories')

        else:
            messages.error(request, "Please enter a category name.")

    return render(request, 'books/add_category.html', {'back_url': back_url})


@login_required
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


@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted successfully!")
        return redirect('home')
    messages.error(request, "Invalid request method.")
    return redirect('home')


@login_required
def manage_categories(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        if 'save_changes' in request.POST:
           
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
                    messages.success(request, "Selected categories deleted successfully ❎")
                except ProtectedError:
                    messages.error(request, "Cannot delete some categories because they are linked to existing books 📚")

        return redirect('manage_categories')

    return render(request, 'books/manage_categories.html', {'categories': categories})

@login_required
def delete_categories(request):
    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('delete_ids')
        if ids_to_delete:
            Category.objects.filter(id__in=ids_to_delete).delete()
    return redirect('manage_categories')



def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    comments = Comment.objects.filter(book=book)

    visitor_comments = request.session.get('visitor_comments', [])

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()

            if not request.user.is_authenticated:
                visitor_comments.append(comment.id)
                request.session['visitor_comments'] = visitor_comments

            return redirect('book_detail', id=book.id)
    else:
        form = CommentForm()

    context = {
        'book': book,
        'comments': comments,
        'form': form,
        'visitor_comments': visitor_comments
    }
    return render(request, 'books/book_detail.html', context)




@login_required
def add_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_book = form.save()
        # لكل مستخدم عادي: سجل الكتاب في السشن
        if not request.user.is_superuser:
            my_books = request.session.get('my_books', [])
            if new_book.id not in my_books:
                my_books.append(new_book.id)
                request.session['my_books'] = my_books
        messages.success(request, "Book added successfully!")
        return redirect('home')
    
    return render(request, 'books/add_book.html', {'form': form})


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    visitor_comments = request.session.get('visitor_comments', [])

    allowed = (request.user.is_authenticated and comment.user == request.user) or \
              (not request.user.is_authenticated and comment.id in visitor_comments)
    if not allowed:
        return JsonResponse({'success': False, 'error': "You can't delete this comment!"}, status=403)

    if request.method == 'POST':
        comment.delete()
        if not request.user.is_authenticated:
            visitor_comments.remove(id)
            request.session['visitor_comments'] = visitor_comments
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request.'}, status=400)


def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    visitor_comments = request.session.get('visitor_comments', [])

    allowed = (request.user.is_authenticated and comment.user == request.user) or \
              (not request.user.is_authenticated and comment.id in visitor_comments)
    if not allowed:
        return JsonResponse({'success': False, 'error': "You can't edit this comment!"}, status=403)

    if request.method == 'POST':
        new_text = request.POST.get('text', '').strip()
        if not new_text:
            return JsonResponse({'success': False, 'error': 'Comment cannot be empty.'}, status=400)
        comment.text = new_text
        comment.save()
        return JsonResponse({'success': True, 'new_text': comment.text})

    return JsonResponse({'success': False, 'error': 'Invalid request.'}, status=400)






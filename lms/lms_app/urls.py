from django.urls import path
from .views import add_category
from .views import user_logout
from .views import edit_category
from .views import delete_category
from . import views

from .views import (
    home,
    about,
    admin_redirect,
    user_login,
    register,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    path('', user_login, name='login'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('admin-redirect/', admin_redirect, name='admin_redirect'),

       
    
    path('books/add-category/', add_category, name='add_category'),
    path('books/add/', add_book, name='add_book'),
    
    path('books/delete/<int:id>/', delete_book, name='delete_book'),
    path('logout/', user_logout, name='logout'),
    path('books/category/edit/<int:id>/', edit_category, name='edit_category'),
    path('books/category/delete/<int:id>/', delete_category, name='delete_category'),
    path('books/manage_categories/', views.manage_categories, name='manage_categories'),
    path('books/delete_categories/', views.delete_categories, name='delete_categories'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),


]

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import edit_comment, delete_comment

urlpatterns = [
    # User Auth
    path('', views.user_login, name='login'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    # Home & About
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin-redirect/', views.admin_redirect, name='admin_redirect'),

    # Books
    path('books/add/', login_required(views.add_book), name='add_book'),
    path('books/edit/<int:book_id>/', login_required(views.edit_book), name='edit_book'),
    path('books/delete/<int:id>/', login_required(views.delete_book), name='delete_book'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),

    # Categories
    path('books/add-category/', login_required(views.add_category), name='add_category'),
    path('books/category/edit/<int:id>/', login_required(views.edit_category), name='edit_category'),
    path('books/category/delete/<int:id>/', login_required(views.delete_category), name='delete_category'),
    path('books/manage_categories/', login_required(views.manage_categories), name='manage_categories'),
    path('books/delete_categories/', login_required(views.delete_categories), name='delete_categories'),

    path('comment/edit/<int:id>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:id>/', delete_comment, name='delete_comment'),
]

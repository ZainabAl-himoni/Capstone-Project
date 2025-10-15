from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    STATUS_BOOK = [
        ('available', 'Available'),
        ('rental', 'Rental'),
        ('sold', 'Sold'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    photo_book = models.ImageField(upload_to='book', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_BOOK, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    rating = models.FloatField(default=0)  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  
    name = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name or 'Anonymous'} - {self.book.title}"

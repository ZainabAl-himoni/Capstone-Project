from django.contrib import admin
from django.contrib.auth.models import Group, User
from django import forms
from .models import Category, Book

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "NestBooks"
admin.site.site_title = "NestBooks Portal"
admin.site.index_title = "Manage NestBooks Content"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.fields:
            self.fields['category'].widget.can_add_related = False
            self.fields['category'].widget.can_change_related = False
            self.fields['category'].widget.can_delete_related = False
            self.fields['category'].widget.can_view_related = False

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title', 'category', 'price', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'author')

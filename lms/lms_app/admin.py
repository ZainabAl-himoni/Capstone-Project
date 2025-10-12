from django.contrib import admin
from django.contrib.auth.models import Group, User
from django import forms
from .models import Category, Book

# 1️⃣ إخفاء Users و Groups من لوحة الإدارة
admin.site.unregister(Group)
admin.site.unregister(User)

# 2️⃣ تخصيص عناوين لوحة الإدارة
admin.site.site_header = "NestBooks"
admin.site.site_title = "NestBooks Portal"
admin.site.index_title = "Manage NestBooks Content"

# 3️⃣ تسجيل نموذج Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# 4️⃣ نموذج مخصص لـ Book لتعديل الـ widget
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # إخفاء أزرار "Add / Change / Delete / View" بجانب الـ ForeignKey
        if 'category' in self.fields:
            self.fields['category'].widget.can_add_related = False
            self.fields['category'].widget.can_change_related = False
            self.fields['category'].widget.can_delete_related = False
            self.fields['category'].widget.can_view_related = False

# 5️⃣ تسجيل نموذج Book مع النموذج المخصص
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title', 'category', 'price', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'author')

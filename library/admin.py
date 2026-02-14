from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'title', 'author', 'price')
    search_fields = ('title', 'author')
    list_filter = ('author',)

"""
Administrator
"""
from django.contrib import admin
from .models import Book
from .models import Login


class BookAdmin(admin.ModelAdmin):
    """ Model class for admin """
    list_display = ('title', 'authors', 'description', 'is_in_stock')


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Login)

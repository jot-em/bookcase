from django.contrib import admin
from .models import Book, BookLocation

# Register your models here.

admin.site.register(Book)
admin.site.register(BookLocation)
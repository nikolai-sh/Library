from django.contrib import admin

# Register your models here.
from .models import Book, BookInstance, Author, Genre, Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)

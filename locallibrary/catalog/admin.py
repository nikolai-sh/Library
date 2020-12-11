from django.contrib import admin

# Register your models here.
from .models import Book, BookInstance, Author, Genre, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

#  Add an inline listing of Book items to the Author    
class BooksInline(admin.TabularInline):
    model = Book


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 #to have NO spare book instances 

# Register the Admin classes for Book using the decorator
# this does exactly the same thing as the admin.site.register() syntax
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrowed', 'due_back','id')

    #  Add "sections" to group related model information within the detail form
    # using fieldsets
    fieldsets = (
        (None, {
            "fields": ('book', 'imprint', 'id'),
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )



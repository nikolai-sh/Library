from django.db import models
from django.shortcuts import render

# Create your views here.
from catalog.models import Book, BookInstance, Author, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #  The 'all()' is implied by default 
    num_authors = Author.objects.all().count()
    # Create list of pairs ['Genre', 'Books']
    # num_genre_books = ([genre, books] for Book.objects.filter(genre__exact='genre').count()
    genre_list = Genre.objects.all()
    genre_books = {}
    for genre in range(len(genre_list)):
        genre_books[genre_list[genre].name] = Book.objects.filter(genre__name=genre_list[genre].name).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'genre_books': genre_books,
    }

     # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# from django.views import generic

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
        # return Book.objects.all()[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
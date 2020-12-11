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

     # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    # Create list of pairs ['Genre', 'Books']
    # num_genre_books = ([genre, books] for Book.objects.filter(genre__exact='genre').count()
    def genre_count_books():
        '''
            Return dict {'Genre': count_books}
        '''
        genre_list = Genre.objects.all()
        genre_books = {}
        
        for genre in range(len(genre_list)):
            genre_books[genre_list[genre].name] = Book.objects.filter(genre__name=genre_list[genre].name).count()
        return genre_books
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'genre_count_books': genre_count_books,
    }

     # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html', 
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,
                'num_authors':num_authors, 'genre_count_books': genre_count_books,
                'num_visits':num_visits}, # num_visits appended
    )
# from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10 #for pagination
    # template_name = 'book_list.html'

    # def get_queryset(self):
    #     # return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    #     return Book.objects.all()

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    # template_name = "author_list.html"

class AuthorDetailView(generic.DetailView):
    model = Author

    

from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

from django.contrib.auth.mixins import PermissionRequiredMixin

class AllBorrowedBooksView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.can_mark_returned'
    # Or multiple permissions
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    # Note that 'catalog.can_edit' is just an example
    # the catalog application doesn't have such permission!
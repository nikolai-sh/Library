# Django Local Library

Tutorial "Local Library" website written in Django.

For detailed information about this project see the associated [MDN tutorial home page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website).

## Overview

This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

* There are models for books, book copies, genre, language and authors.
* Users can view list and detail information for books and authors.
* Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
* Librarians can renew reserved books

### № Module 
   *  Exercises 

1. Using models.
   * Create Language model. 
2.  Django admin site.
   * For the BookInstance list view, add code to display the book, status, due back date, and id (rather than the default __str__() text).
   * Add an inline listing of Book items to the Author detail view using the same approach as we did for Book/BookInstance.
3. Creating our home page.
   * The LocalLibrary base template includes a title block. Override this block in the index template and create a new title for the page. 
   * Modify the view to generate counts for genres and books that contain a particular word (case insensitive), and pass the results to the context.
4. Generic list and detail views.
   * Create the author detail and list views required to complete the project. 
   * The code required for the URL mappers and the views should be virtually identical to the Book list and detail views we created above.
5. Sessions framework.(Without exercises) 
## TODO
6. User authentication and permissions.
7. Working with forms.
8. Testing a Django web application.
9. Deploying Django to production.

## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   Recommended using a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   pip3 install -r requirements.txt
   <!-- python3 manage.py test # Run the standard tests. These should all pass. TODO -->
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.

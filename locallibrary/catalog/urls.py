from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('books/', views.BookListView.as_views(), name="books" ),
]

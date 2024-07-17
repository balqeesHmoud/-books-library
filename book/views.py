from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book

# Create your views here.
class HomePageViews(TemplateView):
    # Process this req (home req)
    template_name = 'home.html'

class ListOfBooksPageViews(ListView):
    # Process this req (books list req)
    model = Book
    template_name = 'list_of_books.html'
    context_object_name = 'books'

class BookDetailsViews(DetailView):
    # Process this req (book details req)
    model = Book
    template_name = 'books_details.html'
    context_object_name = 'book'

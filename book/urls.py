#urls for this app
from django.contrib import admin
from django.urls import path
from .views import HomePageViews, ListOfBooksPageViews, BookDetailsViews

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomePageViews.as_view(), name='home'),
    path('list_of_books/', ListOfBooksPageViews.as_view(), name='books'),
    path('books_details/<int:pk>/', BookDetailsViews.as_view(), name='books_details'),
]
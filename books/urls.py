from django.urls import path
from books.views import IndexView, BookDetailView, GenreView, AddBookView, UpdateBookView, DeleteBookView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', AddBookView.as_view(), name='add'),
    path('<slug:slug>/update/', UpdateBookView.as_view(), name='update'),
    path('<slug:slug>/delete/', DeleteBookView.as_view(), name='delete'),

    path('g/<str:genre>/', GenreView.as_view(), name='genre'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail')
]
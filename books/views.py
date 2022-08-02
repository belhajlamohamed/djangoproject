from pyexpat import model
from django.shortcuts import render
# from django.views.generic.base  import TemplateView
from django.views.generic.detail  import DetailView
from django.views.generic.list  import ListView
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from .models import Book
from django.db.models import F
from django.utils import timezone
from .forms import AddForm

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    context_object_name = 'book'
    
    success_url = '/books/'

class UpdateBookView(UpdateView):
    model = Book
    form_class = AddForm
    template_name = 'books/add.html'
    success_url = '/books/'


# class AddBookView(FormView):
#     template_name = 'add.html'
#     form_class = AddForm
#     success_url = '/books/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class AddBookView(CreateView):
    model = Book
    # fields = ['title', 'genre', 'author', 'isbn']
    form_class = AddForm
    template_name = 'books/add.html'
    success_url = '/books/'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['title'] = 'Enter Title'
        return initial

class IndexView(ListView):
    model = Book
    template_name = "books/home.html"
    # queryset = Book.objects.all()[:4]
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        return Book.objects.all()

class GenreView(ListView):
    model = Book
    template_name = "books/home.html"
    # queryset = Book.objects.all()[:4]
    context_object_name = 'books'
    # paginate_by = 2

    def get_queryset(self,*args, **kwargs):
        return Book.objects.filter(genre__icontains=self.kwargs.get('genre'))
    

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['books'] = Book.objects.all()
    #     return context

# class IndexView(TemplateView):
#     template_name = "home.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Book.objects.all()
#         return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book-detail.html'
    context_object_name = 'book'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Book.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)
        context['time'] = timezone.now()

        return context
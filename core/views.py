from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from core.models import Book, Author, Category
from .forms import BookForm
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    """
    The function home() takes a request as an argument and returns a response

    :param request: The request is an HttpRequest object. It contains metadata about the request, such
    as the client’s IP address, the HTTP method, and the headers
    :return: The home.html file
    """
    return render(request, 'core/home.html')

class bookListView(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('book_edit', args=[self.object.isbn]) + '?ok'


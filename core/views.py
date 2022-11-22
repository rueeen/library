
from django.shortcuts import render
from core.models import Book, Author, Category
from .forms import BookForm

# Create your views here.

def home(request):
    """
    The function home() takes a request as an argument and returns a response
    
    :param request: The request is an HttpRequest object. It contains metadata about the request, such
    as the client’s IP address, the HTTP method, and the headers
    :return: The home.html file
    """
    return render(request, 'core/home.html')

def book_list(request):
    """
    It takes a request, gets all the books from the database, and returns a rendered template with the
    list of books
    
    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: A list of books
    """
    listado = Book.objects.all()
    context = {'context': listado}
    return render(request, 'core/book_list.html', context)

def book_register(request):
    """
    It creates a new instance of the BookForm class, and passes it to the template
    
    :param request: The request object is a parameter that Django automatically passes to all views. It
    contains metadata about the request, such as the HTTP method, the URL, the client's IP address, and
    so on
    :return: The book_register function is returning the book_register.html template.
    """
    book_form = BookForm()
    return render(request, 'core/book_register.html', {'form':book_form})

def book_created(request):
    """
    A function that is called when a book is created.
    
    :param request: The request object
    """
    book_form = BookForm(data=request.POST)
    context = {'context': 'Se ha producido un error'}  
    #this validate the form request  
    if book_form.is_valid():
        #Instance of Book
        b = Book()
        #Setting attributes
        b.isbn = request.POST.get('isbn')
        b.title = request.POST.get('title')
        b.year = request.POST.get('year')
        b.description = request.POST.get('description')
        author = request.POST.get('author')
        #Foreing key asotiation
        #Model.objects.get(pk) find the model with the pk send by parameter
        a = Author.objects.get(name=author)
        b.author = a
        #Save the class and create a row in BD. WE MUST DO SAVE BEFORE ADD
        b.save()
        #many to many asotiation     
        #Here we take the list from the multiselect  with getlist 
        categoryes = request.POST.getlist('category')
        for c in categoryes:
            #
            cat = Category.objects.get(id=c)
            #Add to the created book the category from the list
            b.category.add(cat)      
        #Update the key "context" ant set a new message  
        context.update({'context': 'Libro creado'})
    return render(request, 'core/book_created.html', context)

def book_deleted(request):
    """
    It renders the book_deleted.html template, which is a page that says "Book deleted!"
    
    :param request: The request is an HttpRequest object. It contains metadata about the request, such
    as the HTTP method
    :return: The book_deleted.html page is being returned.
    """
    context = {'context': None}
    return render(request, 'core/book_deleted.html', context)


def book_edit(request):
    context = {'context': None}
    return render(request, 'core/book_edit.html', context)

def book_edited(request):
    context = {'context': None}
    return render(request, 'core/book_edited.html', context)

from django import forms
from .models import Author, Category
from ckeditor.fields import RichTextField

# It creates a form with the fields specified in the class.
class BookForm(forms.Form):

    # Creating a form field with the name `isbn` and the type `CharField`.
    isbn = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'input form-control'}
    ))
    # Creating a form field with the name `title` and the type `CharField`.
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'input form-control'}
    ))
    # Creating a form field with the name `year` and the type `DateField`.
    year = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class':'date form-control'}
    ))
    # Creating a form field with the name `description` and the type `CharField`.
    description = forms.CharField(label="Descripción", required=True, widget=forms.Textarea(
        attrs={'class':'form-control'}
    ))
    # Creating a form field with the name `category` and the type `ModelMultipleChoiceField`.
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'select form-control'}
    ))
    # Creating a form field with the name `author` and the type `ModelChoiceField`.
    author = forms.ModelChoiceField(Author.objects.all(), widget=forms.Select(
        attrs={'class': 'select form-control'}
    ))


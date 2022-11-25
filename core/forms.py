from django import forms
from .models import Author, Category, Book

# It creates a form with the fields specified in the class.

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'year', 'description', 'category', 'author']
        widgets = {
            'isbn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Isbn'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'year': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'select form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
        }
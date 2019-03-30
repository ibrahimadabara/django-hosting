from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title', 'book_author', 'book_pdf')

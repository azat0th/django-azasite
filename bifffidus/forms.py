from django import forms
from .models import Movie, Person

class MovieSearchForm(forms.Form):
    movie_title = forms.CharField(label='Title', max_length=150)
    
class PersonSearchForm(forms.Form):
    person_name = forms.CharField(label='Name', max_length=150)
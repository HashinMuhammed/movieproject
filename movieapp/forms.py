from django import forms
from . models import movieslist

class Movieforms(forms.ModelForm):
    class Meta:
        model=movieslist
        fields=['name','desc','img','year']
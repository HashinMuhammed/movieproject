from django import views
from django.http import HttpResponse
from django.shortcuts import render,redirect

from movieapp.forms import Movieforms
from . models import movieslist
from django import forms


# Create your views here.
def index(request):
    obj=movieslist.objects.all()
    return render(request,"index.html",{'result':obj})

def deatil(request,movielink):
    movie=movieslist.objects.get(id=movielink)
    return render(request,"detail.html",{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movies=movieslist(name=name,desc=desc,year=year,img=img)
        movies.save()
    return render(request,"add.html")

def update(request,id):
    movie=movieslist.objects.get(id=id)
    form=Movieforms(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')    
    
    return render(request,"edit.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=movieslist.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")

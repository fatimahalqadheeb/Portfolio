from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest):
    return render(request, 'Home/home.html')


def about(request: HttpRequest):
    return render(request, 'Home/about.html')


def projects(request: HttpRequest):
    return render(request, 'Home/projects.html')

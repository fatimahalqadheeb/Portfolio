from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest):
    return render(request, 'Home/home.html')
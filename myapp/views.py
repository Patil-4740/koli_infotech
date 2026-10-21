
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Sections")

def about(request):
    return HttpResponse("About Sections")

def contact(request):
    return HttpResponse("Contact Section")


# Create your views here:

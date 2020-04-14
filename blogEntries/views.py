from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogEntry


# Create your views here.
class HomeView(ListView):
    model = BlogEntry
    template_name = 'blogEntries/index.html'
    

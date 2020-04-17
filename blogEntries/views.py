from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogEntry


# Create your views here.
class HomeView(LoginRequiredMixin ,ListView):
    model = BlogEntry
    template_name = 'blogEntries/index.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 3

class EntryView(LoginRequiredMixin, DetailView):
    model = BlogEntry
    template_name = 'blogEntries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin, CreateView):
    model = BlogEntry
    template_name = 'blogEntries/create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)

    

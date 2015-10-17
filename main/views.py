from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from main.models import Genres


class GenreListView(ListView):
    model = Genres
    template_name = 'genres_list.html'
    # context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genres
    slug_field = 'genre_handle'
    template_name = 'genres_detail.html'


class GenreCreateView(CreateView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_create.html'
    success_url = '/genres_list'

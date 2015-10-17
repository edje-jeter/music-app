from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from main.models import Genres, Artists, Albums, Tracks


# ---- models.py Genres -----------------------------
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


# ---- models.py Artists -----------------------------
class ArtistListView(ListView):
    model = Artists
    template_name = 'artists_list.html'


class ArtistDetailView(DetailView):
    model = Artists
    slug_field = 'artist_handle'
    template_name = 'artists_detail.html'


class ArtistCreateView(CreateView):
    model = Artists
    fields = '__all__'
    template_name = 'artists_create.html'
    success_url = '/artists_list'


# ---- models.py Albums -----------------------------
class AlbumListView(ListView):
    model = Albums
    template_name = 'albums_list.html'


class AlbumDetailView(DetailView):
    model = Albums
    slug_field = 'album_handle'
    template_name = 'albums_detail.html'


class AlbumCreateView(CreateView):
    model = Albums
    fields = '__all__'
    template_name = 'albums_create.html'
    success_url = '/albums_list'


# ---- models.py Tracks -----------------------------
class TrackListView(ListView):
    model = Tracks
    template_name = 'tracks_list.html'


class TrackDetailView(DetailView):
    model = Tracks
    slug_field = 'track_handle'
    template_name = 'tracks_detail.html'


class TrackCreateView(CreateView):
    model = Tracks
    fields = '__all__'
    template_name = 'tracks_create.html'
    success_url = '/tracks_list'

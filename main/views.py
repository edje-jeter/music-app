from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from main.models import Genres, Artists, Albums, Tracks

from main.models import CustomUser
from main.forms import UserSignUp, UserLogin

from django.contrib.auth import authenticate, login, logout


def signup(request):
    context = {}

    form = UserSignUp()
    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = CustomUser.objects.create_user(email, password)

                auth_user = authenticate(email=email, password=password)

                login(request, auth_user)

                return HttpResponseRedirect('/')

            except IntegrityError, e:
                context['valid'] = "A User with that name already exists."

        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/')


def login_view(request):
    context = {}

    context['form'] = UserLogin()

    if request.method == 'POST':
        form = UserLogin(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            auth_user = authenticate(email=email, password=password)

            if auth_user is not None:
                login(request, auth_user)

                return HttpResponseRedirect('/')

            else:
                context['valid'] = "Invalid User"

        context['valid'] = "Please enter a User name"

    return render_to_response('login.html', context, context_instance=RequestContext(request))

# ---- About page; uses Genres model as a placeholder ------------------
class AboutView(ListView):
    model = Genres
    template_name = 'about.html'


# ---- models.py Genres -----------------------------
class GenreListView(ListView):
    model = Genres
    template_name = 'genres_list.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genres
    slug_field = 'genre_handle'
    template_name = 'genres_detail.html'
    context_object_name = 'genres'


class GenreCreateView(CreateView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_create.html'
    success_url = '/genres_list'
    context_object_name = 'genres'


# ---- models.py Artists -----------------------------
class ArtistListView(ListView):
    model = Artists
    template_name = 'artists_list.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artists
    slug_field = 'artist_handle'
    template_name = 'artists_detail.html'
    context_object_name = 'artists'


class ArtistCreateView(CreateView):
    model = Artists
    fields = '__all__'
    template_name = 'artists_create.html'
    success_url = '/artists_list'
    context_object_name = 'artists'


# ---- models.py Albums -----------------------------
class AlbumListView(ListView):
    model = Albums
    template_name = 'albums_list.html'
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Albums
    slug_field = 'album_handle'
    template_name = 'albums_detail.html'
    context_object_name = 'albums'


class AlbumCreateView(CreateView):
    model = Albums
    fields = '__all__'
    template_name = 'albums_create.html'
    success_url = '/albums_list'
    context_object_name = 'albums'


# ---- models.py Tracks -----------------------------
class TrackListView(ListView):
    model = Tracks
    template_name = 'tracks_list.html'
    context_object_name = 'tracks'


class TrackDetailView(DetailView):
    model = Tracks
    slug_field = 'track_id'
    template_name = 'tracks_detail.html'
    context_object_name = 'tracks'


class TrackCreateView(CreateView):
    model = Tracks
    fields = '__all__'
    template_name = 'tracks_create.html'
    success_url = '/tracks_list'
    context_object_name = 'tracks'


# ---- forms.py MusicSearchForm -----------------------------
def music_search(request):
    context = {}

    form = MusicSearchForm()

    context['music_search_v'] = form

    if request.method == 'POST':
        form = MusicSearchForm(request.POST)

        if form.is_valid():
            artists_search = Artists.objects.filter(name__icontains=form.cleaned_data['search_music'])
            # albums_search = Albums.objects.filter(name__icontains=form.cleaned_data['search_music'])
            # tracks_search = Tracks.objects.filter(name__icontains=form.cleaned_data['search_music'])
            # genres_search = Genres.objects.filter(name__icontains=form.cleaned_data['search_music'])

            context['artists_search_res'] = artists_search
            # context['albums_search_res'] = albums_search
            # context['tracks_search_res'] = tracks_search
            # context['genres_search_res'] = genres_search

        else:
            context['errors'] = form.errors

    return render_to_response('music_search.html', context,
                              context_instance=RequestContext(request))

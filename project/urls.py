from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^genres_list/$', views.GenreListView.as_view()),
    # url(r'^genres_detail/(?P<pk>\d+)/$', views.GenreDetailView.as_view()),
    url(r'^genres_detail/(?P<slug>.+)/$', views.GenreDetailView.as_view()),
    url(r'^genres_create/$', views.GenreCreateView.as_view()),

    url(r'^artists_list/$', views.ArtistListView.as_view()),
    url(r'^artists_detail/(?P<slug>.+)/$', views.ArtistDetailView.as_view()),
    url(r'^artists_create/$', views.ArtistCreateView.as_view()),

    url(r'^albums_list/$', views.AlbumListView.as_view()),
    url(r'^albums_detail/(?P<slug>.+)/$', views.AlbumDetailView.as_view()),
    url(r'^albums_create/$', views.AlbumCreateView.as_view()),

    url(r'^tracks_list/$', views.TrackListView.as_view()),
    url(r'^tracks_detail/(?P<slug>.+)/$', views.TrackDetailView.as_view()),
    url(r'^tracks_create/$', views.TrackCreateView.as_view()),

    url(r'^about/$', views.AboutView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

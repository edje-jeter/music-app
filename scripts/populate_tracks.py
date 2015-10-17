#!/usr/bin/env python
import os
import sys
import requests
from unidecode import unidecode
from PIL import Image
from StringIO import StringIO

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Genres, Artists, Albums, Tracks

Tracks.objects.all().delete()
artists_in_db = Artists.objects.all()

for artist in artists_in_db:
    print "=============================================================="
    albums_url = "https://freemusicarchive.org/api/get/tracks.json?api_key=GHPJJTZVUKT1DZB1&artist_id="
    current_artist_id = artist.artist_id
    url_w_artist_id = str(albums_url) + str(current_artist_id)
    print url_w_artist_id
    response = requests.get(url_w_artist_id)
    response_dict = response.json()

    for data in response_dict['dataset']:
        new_track, created = Tracks.objects.get_or_create(track_id=int(data.get('track_id')))

        if data.get('track_title') != None:
            new_track.track_title = str(unidecode(data.get('track_title')))

        if data.get('track_url') != None:
            new_track.track_url = str(unidecode(data.get('track_url')))

        if data.get('track_duration') != None:
            new_track.track_duration = str(unidecode(data.get('track_duration')))

        if data.get('track_number') != None:
            new_track.track_number = int(data.get('track_number'))

        try:
            new_track_image = requests.get(data.get('track_image_file'))
            temp_image = NamedTemporaryFile(delete=True)
            temp_image.write(new_track_image.content)
            new_track.track_image_file = File(temp_image)
        except Exception, e:
            print e

        try:
            new_track.track_artist_id = Artists.objects.get(artist_id=current_artist_id)
        except Exception, e:
            new_track.track_artist_id = None

        try:
            current_album_id = str(data.get('album_id'))
            new_track.track_album_id = Albums.objects.get(album_id=current_album_id)
        except Exception, e:
            new_track.track_artist_id = None

        if data.get('track_genres') != None:
            genres = data.get('track_genres')
            for genre in genres:
                genre_id = genre['genre_id']
                genre_obj, created = Genres.objects.get_or_create(genre_id=genre_id)
                new_track.track_genre_id.add(genre_obj)

        # try:
        #     album_artist_object, created = Artists.objects.get_or_create(artist_name=current_album_artist_name)
        #     new_album.album_artist_id = album_artist_object
        # except Exception, e:
        #     print e

        new_track.save()
        print "Artist: %s" % artist.artist_name
        print "---Track: %s" % new_track.track_title

Tracks.objects.filter(track_artist_id__artist_id=None).delete()

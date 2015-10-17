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
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Genres, Artists, Albums

artists_in_db = Artists.objects.all()

for artist in artists_in_db:
    print "=============================================================="
    albums_url = "https://freemusicarchive.org/api/get/albums.json?api_key=GHPJJTZVUKT1DZB1&artist_id="
    current_artist_id = str(artist.artist_id)
    url_w_artist_id = str(albums_url) + current_artist_id
    print url_w_artist_id
    response = requests.get(url_w_artist_id)
    response_dict = response.json()

    for data in response_dict['dataset']:
        new_album, created = Albums.objects.get_or_create(album_id=int(data.get('album_id')))

        if data.get('album_title') != None:
            new_album.album_title = str(unidecode(data.get('album_title')))

        if data.get('album_handle') != None:
            new_album.album_handle = str(data.get('album_handle'))

        if data.get('album_producer') != None:
            new_album.album_producer = str(unidecode(data.get('album_producer')))

        if data.get('album_engineer') != None:
            new_album.album_engineer = str(unidecode(data.get('album_engineer')))

        if data.get('album_date_released') != None:
            new_album.album_date_released = str(unidecode(data.get('album_date_released')))

        if data.get('album_tracks') != None:
            new_album.album_tracks = int(data.get('album_tracks'))

        try:
            new_album_image = requests.get(data.get('album_image_file'))
            temp_image = NamedTemporaryFile(delete=True)
            temp_image.write(new_album_image.content)
            new_album.album_image_file = File(temp_image)
        except Exception, e:
            print e

        try:
            new_album.album_artist_id = Artists.objects.get(artist_id=current_artist_id)
        except Exception, e:
            new_album.album_artist_id = None

        # try:
        #     album_artist_object, created = Artists.objects.get_or_create(artist_name=current_album_artist_name)
        #     new_album.album_artist_id = album_artist_object
        # except Exception, e:
        #     print e

        new_album.save()
        print "Artist: %s" % artist.artist_name
        print "---Album: %s" % new_album.album_title

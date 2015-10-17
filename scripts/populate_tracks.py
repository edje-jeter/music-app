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

from main.models import Genres, Artists, Albums, Tracks

print "=============================================================="
response = "https://freemusicarchive.org/api/get/tracks.json?api_key=GHPJJTZVUKT1DZB1&limit=100"

response_dict = response.json()

for data in response_dict['dataset']:
    new_track, created = Tracks.objects.get_or_create(track_id=int(data.get('track_id')))

    if data.get('track_title') != None:
        new_track.track_title = str(data.get('track_title'))

    if data.get('track_url') != None:
        new_track.track_url = str(data.get('track_url'))

    if data.get('track_duration') != None:
        new_track.track_duration = str(data.get('track_duration'))

    if data.get('track_number') != None:
        new_track.track_number = int(data.get('track_number'))

    if data.get('track_tracks') != None:
        new_track.track_tracks = int(data.get('track_tracks'))

    try:
        new_track_image = requests.get(data.get('track_image_file'))
        temp_image = NamedTemporaryFile(delete=True)
        temp_image.write(new_track_image.content)
        new_track.new_track_image = File(temp_image)
    except Exception, e:
        print e

    if data.get('track_artist_id') != None:
        new_track.track_artist_id = int(data.get('track_artist_id'))

    if data.get('track_album_id') != None:
        new_track.track_album_id = int(data.get('track_album_id'))

    new_track.save()
    print "Artist: %s" % artist.artist_name
    print "---Track: %s" % new_track.track_title

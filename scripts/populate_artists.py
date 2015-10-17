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

from main.models import Artists

response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=GHPJJTZVUKT1DZB1&limit=100')

response_dict = response.json()

for data in response_dict['dataset']:
    new_artist, created = Artists.objects.get_or_create(artist_id=int(data.get('artist_id')))

    if data.get('artist_handle') != None:
        new_artist.artist_handle = str(data.get('artist_handle'))

    if data.get('artist_url') != None:
        new_artist.artist_url = str(data.get('artist_url'))

    if data.get('artist_name') != None:
        new_artist.artist_name = str(unidecode(data.get('artist_name')))

    if data.get('artist_members') != None:
        new_artist.artist_members = str(unidecode(data.get('artist_members')))

    if data.get('artist_website') != None:
        new_artist.artist_website = str(unidecode(data.get('artist_website')))

    if data.get('artist_wikipedia_page') != None:
        new_artist.artist_wikipedia_page = str(unidecode(data.get('artist_wikipedia_page')))

    try:
        new_artist_image = requests.get(data.get('artist_image_file'))
        temp_image = NamedTemporaryFile(delete=True)
        temp_image.write(new_artist_image.content)
        new_artist.artist_image_file = File(temp_image)
    except Exception, e:
        print e

    print new_artist.artist_name
    new_artist.save()

# try:
#     album_artist_object, created = Artists.objects.get_or_create(artist_name=current_album_artist_name)
#     new_album.album_artist_id = album_artist_object
# except Exception, e:
#     print e

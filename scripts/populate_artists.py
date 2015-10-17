#!/usr/bin/env python
import os
import sys
import requests
from unidecode import unidecode

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Artists


response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=GHPJJTZVUKT1DZB1&limit=500')

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

    if data.get('artist_location') != None:
        new_artist.artist_location = str(unidecode(data.get('artist_location')))

    if data.get('artist_active_year_begin') != None:
        new_artist.artist_active_year_begin = int(data.get('artist_active_year_begin'))

    if data.get('artist_active_year_end') != None:
        new_artist.artist_active_year_end = int(data.get('artist_active_year_end'))

    if data.get('artist_image_file') != None:
        new_artist.artist_image_file = str(data.get('artist_image_file'))

    # new_artist.artist_images = data['artist_images']

    print data['artist_id']
    new_artist.save()

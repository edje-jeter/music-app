from django.contrib import admin

from main.models import Genres
from main.models import Artists
from main.models import Albums
from main.models import Tracks


admin.site.register(Genres)
admin.site.register(Artists)
admin.site.register(Albums)
admin.site.register(Tracks)

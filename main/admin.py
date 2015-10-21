from django.contrib import admin

from main.models import Genres
from main.models import Artists
from main.models import Albums
from main.models import Tracks
from main.models import CustomUser


admin.site.register(Genres)
admin.site.register(Artists)
admin.site.register(Albums)
admin.site.register(Tracks)
admin.site.register(CustomUser)

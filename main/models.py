from django.db import models


class Genres(models.Model):
    genre_id = models.IntegerField(null=True, blank=True)
    genre_parent_id = models.IntegerField(null=True, blank=True)
    genre_title = models.CharField(max_length=255, null=True, blank=True)
    genre_handle = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.genre_title


class Artists(models.Model):
    artist_id = models.IntegerField(null=True, blank=True)
    artist_handle = models.CharField(max_length=255, null=True, blank=True)
    artist_url = models.CharField(max_length=255, null=True, blank=True)
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    artist_members = models.TextField(null=True, blank=True)
    artist_website = models.CharField(max_length=255, null=True, blank=True)
    artist_wikipedia_page = models.CharField(max_length=255, null=True, blank=True)
    artist_image_file = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.artist_name


class Albums(models.Model):
    album_id = models.IntegerField(null=True, blank=True)
    album_title = models.CharField(max_length=255, null=True, blank=True)
    album_handle = models.CharField(max_length=255, null=True, blank=True)
    album_producer = models.CharField(max_length=255, null=True, blank=True)
    album_engineer = models.CharField(max_length=255, null=True, blank=True)
    album_date_released = models.CharField(max_length=255, null=True, blank=True)
    album_tracks = models.IntegerField(null=True, blank=True)
    album_image_file = models.CharField(max_length=255, null=True, blank=True)
    album_artist_id_obj = models.ForeignKey('main.Artists', null=True, blank=True)

    # Jeff says call album_artist_id ==> album_artist because...
    # 1. ForeignKey turns it into an object rather than just a integer ID; and
    # 2. we want the name "artist" to point the reader to the Artists class,
    # which is where the ForeignKey is pointing us (main.Artists).
    # # album_artist_name = models.ForeignKey('main.Artists', null=True, blank=True)

    def __unicode__(self):
        return self.album_title


class Tracks(models.Model):
    track_id = models.IntegerField(null=True, blank=True)
    track_title = models.CharField(max_length=255, null=True, blank=True)
    track_url = models.CharField(max_length=255, null=True, blank=True)
    track_duration = models.CharField(max_length=255, null=True, blank=True)
    track_number = models.CharField(max_length=255, null=True, blank=True)
    track_image_file = models.CharField(max_length=255, null=True, blank=True)
    track_artist_id_obj = models.ManyToManyField('main.Artists', blank=True)
    track_album_id_obj = models.ForeignKey('main.Albums', null=True, blank=True)

    def __unicode__(self):
        return self.track_title

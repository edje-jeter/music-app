from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


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
    artist_image_file = models.ImageField(upload_to="artist_images", null=True, blank=True)

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
    album_image_file = models.ImageField(upload_to="album_images", null=True, blank=True)
    # album_artist_id = models.IntegerField(null=True, blank=True)
    album_artist_id = models.ForeignKey('main.Artists', null=True, blank=True)

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
    track_image_file = models.ImageField(upload_to="track_images", null=True, blank=True)
    track_artist_id = models.ForeignKey('main.Artists', null=True, blank=True)
    track_album_id = models.ForeignKey('main.Albums', null=True, blank=True)
    track_genre_id = models.ManyToManyField('main.Genres')

    def __unicode__(self):
        return self.track_title

from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin): pass


class ArtistAdmin(admin.ModelAdmin): pass


class LabelAdmin(admin.ModelAdmin): pass


admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Label, LabelAdmin)

from django.contrib import admin
from .models import Artiste, Album, Song



admin.site.site_header = "Smanager"
admin.site.site_title = "Song Manager"
admin.site.index_title = "Welcome To Smanager"

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
	pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	pass

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	pass


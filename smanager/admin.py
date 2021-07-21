from django.contrib import admin
from .models import Artiste, Album, Song



admin.site.site_header = "Smanager"
admin.site.site_title = "Song Manager"
admin.site.index_title = "Welcome To Smanager"

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
	list_display = ('prenom', 'nom', 'birthday', 'country', 'town')
	list_filter = ('birthday', 'country', 'town')
	pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('titre', 'artiste.prenom', 'release_date')
	list_filter = ('titre', 'artiste', 'release_date')
	pass

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	list_display = ('song_title', 'album', 'duration', 'lyrics')
	list_filter = ('album', 'duration')
	pass


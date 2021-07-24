import time
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
	list_display = ('titre', 'nom', 'release_date')
	list_filter = ('titre', 'artiste', 'release_date')
	def nom(self, obj):
		return obj.artiste.prenom, obj.artiste.nom
	pass

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	list_display = ('song_title', 'albums', 'duration_time', 'lyrics')
	list_filter = ('album', 'duration')

	def albums(self, obj):
		return obj.album.titre

	def duration_time(self, obj):
		return time.strftime('%M:%S', time.gmtime(obj.duration))
		duration_time.short_description = 'Duration'
		duration_time.admin_order_field = 'duration'

	pass


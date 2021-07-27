from django.shortcuts import render
#from django.views.generic import ListView
from .models import Song 
import json
from django.http import JsonResponse


"""class IndexListView(ListView):
	model = Song
	template_name = 'smanager/index.html'

	def get_content_data(self, **kwargs):
		context = super().get_content_data(**kwargs)
		context["qs_json"] = json.dumps(list(Song.objects.values))
		return context"""
def autosearch(request):
	songs = request.GET.get('song_title')
	payload = []
	if songs:
		songs_titles = Song.objects.all()

		for song_name in songs_titles:
			payload.append(song_name.song_title)

	return JsonResponse({'status' :200 , 'data' : payload})

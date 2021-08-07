from django.shortcuts import render
#from django.views.generic import ListView
from .models import Song 
#import json
from django.http import JsonResponse
from .models import Song


"""class IndexListView(ListView):
	model = Song
	template_name = 'smanager/index.html'

	def get_content_data(self, **kwargs):
		context = super().get_content_data(**kwargs)
		context["qs_json"] = json.dumps(list(Song.objects.values))
		return context"""
def autosearch(request):
	if 'term' in request.GET:
		#qs = Song.objects.filter(song_title__istartswith=request.GET.get('term'))
		qs = Song.objects.filter(song_title__contains=request.GET.get('term'))
		titles = list()
		for song in qs:
			titles.append(song.song_title)
		return JsonResponse(titles, safe=False)
	return render(request, 'smanager/index.html')


def search_song(request):
	if request.method == "POST":
		search = request.POST['search']
		songsearched = Song.objects.filter(lyrics__contains=search)
		return render(request, 'smanager/search_song.html',{'search':search, 'songsearched':songsearched})
	else:
		return render(request, 'smanager/search_song.html',{})

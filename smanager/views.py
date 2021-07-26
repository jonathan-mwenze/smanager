from django.shortcuts import render
from .models import Song, Artiste

def index(request):
	songs = Artiste.objects.all()
	return render(request, 'smanager/index.html', {'songs':songs})
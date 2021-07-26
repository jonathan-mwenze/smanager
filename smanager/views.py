from django.shortcuts import render
from django.views.generic import ListView
from .models import Song 
import json


class IndexListView(ListView):
	model = Song
	template_name = 'smanager/index.html'

	def get_content_data(self, **kwargs):
		context = super().get_content_data(**kwargs)
		context["qs_json"] = json.dumps(list(Song.objects.values))
		return context
	
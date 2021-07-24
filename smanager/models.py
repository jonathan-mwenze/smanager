from django.db import models

class Artiste(models.Model):
	prenom = models.CharField(max_length=255, help_text="Jonathan")
	nom = models.CharField(max_length=255)
	birthday = models.DateField()
	country = models.CharField(max_length=50)
	town = models.CharField(max_length=60)

	def __str__(self):
		return "{} {} {} {} {} ".format(self.prenom, self.nom, self.birthday, self.country, self.town)

class Album(models.Model):
	titre = models.CharField(max_length=255)
	artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
	release_date = models.DateField()

	def __str__(self):
		return "{} {} {} ".format(self.titre, self.artiste, self.release_date)

class Song(models.Model):
	song_title = models.CharField(max_length=255)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	duration = models.IntegerField(default=0, help_text="Duration in second")
	lyrics = models.TextField(default="Jesus is my fortres")

	def __str__(self):
		return "{} {} {} ".format(self.song_title, self.album, self.duration, self.lyrics)


# Generated by Django 3.1.7 on 2021-07-20 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(help_text='Jonathan', max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=255)),
                ('duration', models.IntegerField(default=0, help_text='Duration in second')),
                ('lyrics', models.TextField(default='Jesus is my fortres')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smanager.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artiste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smanager.artiste'),
        ),
    ]

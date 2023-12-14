from django.views import View
from django.shortcuts import render
from album.models import addAlbumModel
from django.views.generic import ListView

class homeView(ListView):
    template_name="home.html"
    model=addAlbumModel
    context_object_name='data'
    
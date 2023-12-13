from django.urls import path
from . import views

urlpatterns=[
    path("addAlbum/", views.addAlbumView.as_view(), name="addAlbum"),
   
]
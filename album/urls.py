from django.urls import path
from . import views

urlpatterns=[
    path("addAlbum/", views.addAlbumView.as_view(), name="addAlbum"),
    path("edit/<int:id>/",views.editView.as_view(), name="edit_album"),
    path("delete/<int:id>/",views.deleteView.as_view(), name="delete_album"),
   
]
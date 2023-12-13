from django.urls import path
from . import views

urlpatterns=[
    path("", views.albumView.as_view(), name="album")
]
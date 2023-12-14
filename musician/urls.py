from django.urls import path
from . import views
urlpatterns=[
    path("register/", views.registerView.as_view(), name="register"),
    path("signIn/", views.signInView.as_view(), name="signIn"),
    path("profile/", views.profileView.as_view(), name="profile"),
    path("logOut", views.signOutView.as_view(), name="logOut"),
    path("addMusician/", views.addMusicianView.as_view(), name="addMusician"),
    path("edit_musician/<int:id>/", views.editMusicianView.as_view(), name="edit_musician"),
]
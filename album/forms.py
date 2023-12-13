from django import forms
from . import models

class albumForm(forms.ModelForm):
    class Meta:
        model = models.addAlbumModel
        fields = '__all__'
       
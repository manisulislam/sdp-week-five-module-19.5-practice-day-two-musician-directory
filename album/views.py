from django.shortcuts import render,redirect
from django.views import View
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView,DeleteView
from .models import addAlbumModel
from django.urls import reverse_lazy

# Create your views here.

@method_decorator(login_required, name='dispatch')
class addAlbumView(View):
    template_name = 'addAlbum.html'
    form_class = forms.albumForm
    
    
    def get(self, request):
        return render(request, self.template_name,{"form": self.form_class()})
    
    def post(self, request):
        form=forms.albumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    

@method_decorator(login_required, name='dispatch')
class editView(UpdateView):
    model=addAlbumModel
    form_class=forms.albumForm
    template_name="addAlbum.html"
    success_url=reverse_lazy('profile')
    pk_url_kwarg="id"
    
@method_decorator(login_required, name='dispatch')
class deleteView(DeleteView):
    model=addAlbumModel
    template_name="delete.html"
    success_url=reverse_lazy('profile')
    pk_url_kwarg="id"
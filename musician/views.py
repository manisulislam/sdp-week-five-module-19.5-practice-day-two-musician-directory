from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm,musicianForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from album.models import addAlbumModel
from django.views.generic import UpdateView
from .models import musicianModel
# Create your views here.


class registerView(View):
    template_name = 'register.html'
    form_class= RegistrationForm
    
    
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signIn')
        return render(request, self.template_name, {'form': form})
    

class signInView(LoginView):
    template_name="signIn.html"
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        return super().form_valid(form)
    

class signOutView(LogoutView):
    
    def get_success_url(self):
        return reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class profileView(ListView):
    template_name="profile.html"
    model=addAlbumModel
    context_object_name='data'
    
    
    
    
    

@method_decorator(login_required, name='dispatch')
class addMusicianView(View):
    template_name="addMusician.html"
    form_class=musicianForm
    
    def get(self, request):
        return render(request, self.template_name,{'form': self.form_class()})
    
    def post(self, request):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    

@method_decorator(login_required, name='dispatch')
class editMusicianView(UpdateView):
    model=musicianModel
    form_class=musicianForm
    template_name="addMusician.html"
    success_url=reverse_lazy('profile')
    pk_url_kwarg="id"
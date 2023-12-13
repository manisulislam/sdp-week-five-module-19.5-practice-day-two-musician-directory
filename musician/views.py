from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
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

class profileView(View):
    template_name="profile.html"
    
    def get(self, request):
        return render(request, self.template_name)
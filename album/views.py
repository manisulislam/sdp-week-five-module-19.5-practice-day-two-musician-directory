from django.shortcuts import render,redirect
from django.views import View
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class addAlbumView(View):
    template_name = 'addAlbum.html'
    form_class = forms.albumForm
    
    def get(self, request):
        return render(request, self.template_name,{"form": self.form_class()})
    
    def post(self, request):
        form=forms.addAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('albumList')
        return render(request, self.template_name, {'form': form})
    
   
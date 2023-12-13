from django.shortcuts import render
from django.views import View

# Create your views here.
class albumView(View):
    template_name="album.html"
    
    def get(self,request):
        return render(request,self.template_name)
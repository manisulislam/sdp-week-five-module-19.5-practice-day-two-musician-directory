from django.views import View
from django.shortcuts import render


class homeView(View):
    template_name="home.html"
    
    def get(self, request):
        return render(request, self.template_name)
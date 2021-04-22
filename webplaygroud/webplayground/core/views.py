from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageViews(TemplateView):
    template_name="core/home.html"
    
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name,{'title':"Mi super web"})

class SampleClassViews(TemplateView):
    template_name="core/sample.html"

    


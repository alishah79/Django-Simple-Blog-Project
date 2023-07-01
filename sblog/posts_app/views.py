from django.views.generic import ListView, TemplateView
from .models import Post

class HomePageView(ListView):
    template_name = 'Home.html'
    model = Post
    

class AboutPageView(TemplateView):
    template_name = 'About.html'



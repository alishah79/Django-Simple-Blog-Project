from typing import Any, Optional
from django.db import models
from django.http import Http404
from django.views.generic import ListView, TemplateView, DetailView
from .models import Post

class HomePageView(ListView):
    template_name = 'Home.html'
    queryset = Post.objects.all().order_by('-id')
    context_object_name = 'object_list'
    

class AboutPageView(TemplateView):
    template_name = 'About.html'


class BlogPostsView(ListView):
    template_name = 'Blog.html'
    queryset = Post.objects.all()
    context_object_name = 'object_list'


class PostView(DetailView):
    template_name = 'Post.html'
    
    def get_object(self):
        slug = self.kwargs.get('slug')
        
        try:
            post = Post.objects.get(slug=slug)
        except:
            raise Http404('Post not found!')
        
        return post
from django.urls import path
from .views import *

urlpatterns = [
    path('', view=HomePageView.as_view(), name='home_page'),
    path('about/', view=AboutPageView.as_view(), name='about_page'),
    path('blog/', view=BlogPostsView.as_view(), name='blog'),
    path('blog/<slug:slug>', view=PostView.as_view(), name='blog_post'),
]

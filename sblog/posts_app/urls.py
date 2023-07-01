from django.urls import path
from .views import *

urlpatterns = [
    path('', view=HomePageView.as_view(), name='home_page'),
    path('about/', view=AboutPageView.as_view(), name='about_page'),
]

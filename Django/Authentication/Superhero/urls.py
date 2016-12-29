from rest_framework import mixins
from rest_framework import generics

from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from Superhero import views


urlpatterns = [
    url(r'^Superlist/$', views.heroList.as_view()),


]
urlpatterns = format_suffix_patterns(urlpatterns)
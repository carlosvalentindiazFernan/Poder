from django.shortcuts import render
from Superhero.models import hero
from Superhero.Serializers import SuperSerializer
from rest_framework import generics


class heroList(generics.ListCreateAPIView):
    queryset = hero.objects.all()
    serializer_class = SuperSerializer


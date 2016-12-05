from rest_framework import serializers
from Superhero.models import *

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = hero
        fields = ('name', 'age','power')
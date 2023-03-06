from rest_framework import serializers 
from animals.models import Animal, Species
 
 
class AnimalSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Animal
        fields = ('name',
                  'last_feed_time',
                  'species')
        
class SpeciesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Species
        fields = ('name',)
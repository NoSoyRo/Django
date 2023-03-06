from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.utils import timezone
from rest_framework import status
from .models import Animal, Species
from .serializers import AnimalSerializer, SpeciesSerializer
from rest_framework.parsers import JSONParser 
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers


class AnimalPopulationView(View):
    @csrf_exempt
    def get(self, request):
        print(request)
        nAnimals = Animal.objects.values('name').count()
        return HttpResponse(nAnimals)

@method_decorator(csrf_exempt, name='dispatch')
class AnimalView(View):
    def get(self, request, pk):
        print(pk)
        try: 
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist: 
            return JsonResponse({'message': 'The Animal does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        animal_serializer = AnimalSerializer(animal) 
        return JsonResponse(animal_serializer.data)
    
    def post(self, request):
        animal_data = JSONParser().parse(request)
        nAnimal = Animal.objects.filter(pk = animal_data['name']).count()
        if nAnimal != 0:
            animal_serializer = AnimalSerializer(Animal.objects.get(pk = animal_data['name'])) 
            return JsonResponse(animal_serializer.data)
        specie = Species.objects.filter(pk = animal_data['species']).count()
        if specie == 0:
            specie_data = {'name': animal_data['species']}
            print(specie_data)
            specie_serializer = SpeciesSerializer(data = specie_data)
            if specie_serializer.is_valid():
                specie_serializer.save()
        animal_new_serializer = AnimalSerializer(data = animal_data)
        print(animal_new_serializer)
        if animal_new_serializer.is_valid():
            animal_new_serializer.save()
            return HttpResponse("correct creation", status = status.HTTP_201_CREATED)


class HungryAnimalsView(View):

    def get(self, request):
        prev = datetime.now()-timedelta(days = 2)
        print(prev)
        animal = Animal.objects.filter(last_feed_time__range = ["2023-01-01", prev] )
        print(type(animal))
        animalsUnFed = serializers.serialize("json", Animal.objects.filter(last_feed_time__range = ["2023-01-01", prev]))
        # animal_serializer = AnimalSerializer(animal)
        return HttpResponse(animalsUnFed)


@method_decorator(csrf_exempt, name='dispatch')
class FeedAnimalView(View):
    
    def post(self, request):
        animal_data = JSONParser().parse(request)
        nAnimal = Animal.objects.filter(pk = animal_data['name']).count()
        if nAnimal == 0:
            return HttpResponse("No existe el animal", status = status.HTTP_406_NOT_ACCEPTABLE)
        animal = Animal.objects.get(pk = animal_data['name'])
        animal.last_feed_time = timezone.now()
        animal.save()
        return HttpResponse("Se ha alimentado correctamente el animal")
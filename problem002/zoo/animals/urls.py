from django.urls import re_path
from . import views
 
urlpatterns = [ 
    re_path(r'animalpopulationview/', views.AnimalPopulationView.as_view()),
    re_path(r'animalviewget/(?P<pk>[A-Za-z]+)', views.AnimalView.as_view()),
    re_path(r'animalviewpost/', views.AnimalView.as_view()),
    re_path(r'animalhungryviewget/', views.HungryAnimalsView.as_view()),
    re_path(r'feedanimal/', views.FeedAnimalView.as_view()),
]
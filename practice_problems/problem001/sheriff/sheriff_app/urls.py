from django.urls import re_path
from sheriff_app import views 


urlpatterns = [ 
    re_path(r'customers', views.test_view)
]
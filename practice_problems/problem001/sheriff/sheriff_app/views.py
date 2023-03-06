from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser 
from sheriff_app.serializers import CustomerSerializer
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

FIRST_NAME_VALIDATION_MESSAGE = "First name should only contain characters and numbers without any " \
                                "spaces or special characters"
LAST_NAME_VALIDATION_MESSAGE = "Last name should only contain characters and numbers " \
                               "without any spaces or special characters"
PHONE_VALIDATION_MESSAGE = "Phone number should only contain numbers and should have a maximum length of 10 digits"
EMAIL_VALIDATION_MESSAGE = "Invalid email. Email should have the format: example@domain.com"

@csrf_exempt
def test_view(request):
    if request.method == "GET":
        return HttpResponse("This is a get request")
    elif request.method == "POST":
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data = customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            print(customer_serializer.data)
            return HttpResponse("Se ha creado correctamente el customer", status=status.HTTP_201_CREATED) 
        error = ""
        for values in customer_serializer.errors:
            error += str(customer_serializer.errors[values][0]) + "\n"
        return HttpResponse(error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Bad request", status = status.HTTP_400_BAD_REQUEST)


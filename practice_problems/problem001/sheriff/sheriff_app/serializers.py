from rest_framework import serializers 
from sheriff_app.models import Customer
 
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ('customer_id',
                   'first_name',
                   'last_name',
                   'phone',
                   'email',
                   )
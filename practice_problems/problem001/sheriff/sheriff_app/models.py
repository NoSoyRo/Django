from django.db import models
import sheriff_app.validators as vals

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=200, validators=[vals.validate_first_name], blank = True)
    last_name = models.CharField(max_length=200, validators=[vals.validate_last_name], blank = True)
    phone = models.CharField(max_length=10, validators=[vals.validate_phone], blank = True)
    email = models.CharField(max_length=200, validators=[vals.validate_email], blank = True)

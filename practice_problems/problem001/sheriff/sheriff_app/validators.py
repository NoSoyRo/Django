from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as gtl
import re

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            gtl('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_first_name(value):
    pattern = r"([A-Za-z0-9])*"
    compare = re.compile(pattern)
    a = compare.fullmatch(value)
    if a == None:
        raise ValidationError(
            gtl('First name should only contain characters and numbers without any spaces or special characters')
        )
    
def validate_last_name(value):
    pattern = r"([A-Za-z0-9])*"
    compare = re.compile(pattern)
    a = compare.fullmatch(value)
    if a == None:
        raise ValidationError(
            gtl('Last name should only contain characters and numbers without any spaces or special characters')
        )
    
def validate_phone(value):
    pattern = r"(\d{10})*" 
    compare = re.compile(pattern)
    a = compare.fullmatch(value)
    if a == None:
        raise ValidationError(
            gtl('Phone number should only contain numbers and should have maximum length of 10 digits')
        )   
    
def validate_email(value):
    pattern = r"([A-Za-z0-9_*&^%$#!~?]+@[A-Za-z0-9]+.com)*"
    compare = re.compile(pattern)
    a = compare.fullmatch(value)
    if a == None:
        raise ValidationError(
            gtl('Invalid email. Email should have the format: example@domain.com')
        )
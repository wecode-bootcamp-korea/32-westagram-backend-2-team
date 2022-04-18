import re

from django.core.exceptions import ValidationError

from django.http  import JsonResponse

def blank(email, password):
    if not email or not password:
        raise ValidationError ("KEY_ERROR")

def email_validate(email):
    regexr_email = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regexr_email, email) == None:
        raise ValidationError("ERROR_EMAIL_NEED_@_AND_.")


def password_validate(password):
    regexr_password = '^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[$@$!%*#?&])[A-Za-z0-9$@$!%*#?&].{8,}$'
    if re.match(regexr_password, password) == None:
        raise ValidationError ("ERROR_PASSWORD_STATUS")

def phonenumber_validate(phone_number):
    regexr_phonenumber = '^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$'
    if re.match(regexr_phonenumber, phone_number) == None:
        raise ValidationError ("PHONENUMBER_ERROR")
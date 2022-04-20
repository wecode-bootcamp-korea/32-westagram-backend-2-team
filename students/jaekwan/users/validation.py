import re

from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from users.models import User

EMAIL_REGEX          = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_REGEX       = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
MOBILE_NUMBER_REGEX  = '^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$'

def validate_email(email):
    if not re.match(EMAIL_REGEX, email):
        raise ValidationError("EMAIL_ERROR")

    if User.objects.filter(email=email).exists():
        raise ValidationError("EMAIL_EXISTS_ERROR")

def validate_password(password):
    if not re.match(PASSWORD_REGEX, password):
        raise ValidationError("PASSWORD_ERROR")

def validate_mobile_number(mobile_number):
    if not re.match(MOBILE_NUMBER_REGEX, mobile_number):
        raise ValidationError("MOBILE_NUMBER_ERROR")

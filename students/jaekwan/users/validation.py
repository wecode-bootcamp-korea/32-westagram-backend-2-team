import re
from django.http  import JsonResponse
from users.models import User


EMAIL_REGEX          = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_REGEX       = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
MOBILE_NUMBER_REGEX  = '^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$'

class SignUpValidation:
    def validate_email(email):
        if not re.match(EMAIL_REGEX, email):
            return JsonResponse({"message": "EMAIL_ERROR"}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({"message": "EMAIL_EXISTS_ERROR"}, status=400)

    def validate_password(password):
        if not re.match(EMAIL_REGEX, password):
            return JsonResponse({"message": "PASSWORD_ERROR"}, status=400)

    def validate_mobile_number(mobile_number):
        if not re.match(EMAIL_REGEX, mobile_number):
            return JsonResponse({"message": "MOBILE_NUMBER_ERROR"}, status=400)

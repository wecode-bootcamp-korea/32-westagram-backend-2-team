import json
import re
from django.http  import JsonResponse
from django.views import View

from users.models import User

EMAIL_REGEX          = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_REGEX       = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
MOBILE_NUMBER_REGEX  = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'


class SignupView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            email         = data['email']
            password      = data['password']
            mobile_number = data['mobile_number']

            if not re.match(EMAIL_REGEX, email):
                return JsonResponse({'MESSAGE':'EMAIL_ERROR'}, status=400)

            if not re.match(PASSWORD_REGEX, password):
                return JsonResponse({'MESSAGE':'PASSWORD_ERROR'}, status=400)
            
            if not re.match(MOBILE_NUMBER_REGEX, mobile_number):
                return JsonResponse({'MESSAGE':'MOBILE_NUMBER_ERROR'}, status=400)
            
            User.objects.create(
                name            = data['name'],
                email           = data['email'],
                password        = data['password'],
                mobile_number   = data['mobile_number']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
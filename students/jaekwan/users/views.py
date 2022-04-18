import json
import re
from django.http  import JsonResponse
from django.views import View

from users.models import User

EMAIL_REGEX = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_REGEX = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
MOBILE_NUMBER_REGEX = '\d{3}-\d{3,4}-\d{4}'

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            mobile_number = data['mobile_number']

            if re.match(EMAIL_REGEX, email) == None:
                return JsonResponse({'MESSAGE':'EMAIL_ERROR'}, status=400)

            if re.match(PASSWORD_REGEX, password) == None:
                return JsonResponse({'MESSAGE':'PASSWORD_ERROR'}, status=400)
            
            if re.match(MOBILE_NUMBER_REGEX, mobile_number) == None:
                return JsonResponse({'MESSAGE':'MOBILE_NUMBER_ERROR'}, status=400)

            if email == None or password == None:
                return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except:
            User.objects.create(
                name            = data['name'],
                email           = data['email'],
                password        = data['password'],
                mobile_number   = data['mobile_number']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
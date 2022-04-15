import json
import re
from django.http  import JsonResponse
from django.views import View

from users.models import User

email_regex = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
password_regex = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

class UserSignupView(View):
    '''POST'''
    def post(self, request):
        data = json.loads(request.body)
        if re.match(email_regex, data['email']) == None:
            return JsonResponse({'MESSAGE':'EMAIL_ERROR'}, status=400)

        if re.match(password_regex, data['password']) == None:
            return JsonResponse({'MESSAGE':'PASSWORD_ERROR'}, status=400)

        if data['email'] == None or data['password'] == None:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        User.objects.create(
            name            = data['name'],
            email           = data['email'],
            password        = data['password'],
            mobile_number   = data['mobile_number']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)




























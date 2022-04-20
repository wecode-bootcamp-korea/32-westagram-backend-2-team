import json
import bcrypt

from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.views           import View


from users.models import User
from .validation  import validate_email, validate_password, validate_mobile_number


class SignupView(View):
    def post(self, request):
        try:

            data            = json.loads(request.body)
            email           = data['email']
            password        = data['password']
            mobile_number   = data['mobile_number']
            name            = data['name']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            validate_email(email)
            validate_password(password)
            validate_mobile_number(mobile_number)
            
            User.objects.create(
                name            = name,
                email           = email,
                password        = hashed_password,
                mobile_number   = mobile_number
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        
        except ValidationError as err:
            return JsonResponse({'MESSAGE':err.message}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']

            if User.objects.filter(email = email, password = password).exists():
                return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
            
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)        
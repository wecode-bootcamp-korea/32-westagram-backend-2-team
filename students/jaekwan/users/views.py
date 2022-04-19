import json
import re
from django.http  import JsonResponse
from django.views import View
from users.models import User
from .validation   import SignUpValidation
class SignupView(View):
    def post(self, request):
        try:

            data          = json.loads(request.body)
            email         = data['email']
            password      = data['password']
            mobile_number = data['mobile_number']

            SignUpValidation.validate_email(email)
            SignUpValidation.validate_password(password)
            SignUpValidation.validate_mobile_number(mobile_number)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "EMAIL_EXISTS_ERROR"}, status=400)
            
            User.objects.create(
                name            = data['name'],
                email           = data['email'],
                password        = data['password'],
                mobile_number   = data['mobile_number']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']
            if not email or not password:
                return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)  
            if User.objects.filter(email = email, password = password).exists():
                return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
            
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)        
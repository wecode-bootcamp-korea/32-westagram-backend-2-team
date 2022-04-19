from django.http    import JsonResponse
from django.views   import View
from users.models   import User
import json, re

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email         = data['email']
            password      = data['password']
            mobile_number = data['mobile_number']

            REGEX_EMAIL         = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PASSWORD      = '^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$'
            REGEX_MOBILE_NUMBER = '^([+]\d{2})?\d{10}$'

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({"message": "INVALID_EMAIL"}, status=400)
            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)
            if not re.match(REGEX_MOBILE_NUMBER, mobile_number):
                return JsonResponse({"message": "INVALID_PHONE_NUMBER"}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)

            User.objects.create(
                name 		  = data['name'],
                email	 	  = data['email'],
                password	  = data['password'],
                mobile_number = data['mobile_number'], 
			)

            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']

            if User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message": "SUCCESS"}, status=200)
            else:
                return JsonResponse({"message": "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
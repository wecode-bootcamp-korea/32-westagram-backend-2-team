from django.http import JsonResponse
from django.views import View
import json, re

from users.models import User

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            # name = data['name']
            email = data['email']
            password = data['password']
            mobile_number = data['mobile_number']

            # 정규표현식
            REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PASSWORD = "^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$"
            REGEX_MOBILE_NUMBER = '\d{3}-\d{3,4}-\d{4}'

            # Email Validation
            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({"message": "INVALID_EMAIL"}, status=400)
            # Password Validation
            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)
            # Mobile Number Validation
            if not re.match(REGEX_MOBILE_NUMBER, mobile_number):
                return JsonResponse({"message": "INVALID_PHONE_NUMBER"}, status=400)
            # Email Integrity
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "EMAIL_ALREADY_EXISTS"}, status=400)

            User.objects.create(
                name 		 = data['name'],
                email	 	 = data['email'],
                password	 = data['password'],
                mobile_number = data['mobile_number'], 
			)

            return JsonResponse({"message": "SUCCESS"}, status=201)
        except:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
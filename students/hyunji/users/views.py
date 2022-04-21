import json, re
import bcrypt, jwt

from django.http        import JsonResponse
from django.views       import View
from users.models       import User
from westagram.settings import SECRET_KEY, ALGORITHM

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

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decoded_hashed_password = hashed_password.decode('utf-8')

            User.objects.create(
                name 		  = data['name'],
                email	 	  = data['email'],
                password	  = decoded_hashed_password,
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

            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=401)
            
            access_token = jwt.encode({"id":user.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({
                "message": "SUCCESS", 
                "Authorization":access_token
            }, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status=404)
        
        except User.DoesNotExist:
            return JsonResponse({"MESSAGE": "INVALID_USER"}, status=404)
        
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
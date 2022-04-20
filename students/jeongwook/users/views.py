import json
import bcrypt

from django.http            import JsonResponse
from django.views           import View
from users.models           import User
from .validation            import email_validate, password_validate, phonenumber_validate
from django.core.exceptions import ValidationError

class SignUpView(View):
    def post(self, request):
        data                = json.loads(request.body)
        hashed_password     = bcrypt.hashpw(data['password'].encode('UTF-8'), bcrypt.gensalt())
        
        try: 
            email           = data['email']
            password        = data['password']
            phone_number    = data['phone_number'] 

            email_validate(email)
            password_validate(password)
            phonenumber_validate(phone_number)

            User.objects.create(
                name            = data['name'], 
                email           = data['email'],
                password        = hashed_password,
                phone_number    = data['phone_number'] 
                )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except ValidationError as err:
            return JsonResponse({"message": err.messages}, status=400)


class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try: 
            password = data['password']
            email    = data["email"]

            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

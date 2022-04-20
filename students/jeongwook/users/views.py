import json
import bcrypt, jwt

from django.http            import JsonResponse
from django.views           import View
from users.models           import User
from .validation            import email_validate, password_validate, phonenumber_validate
from django.core.exceptions import ValidationError
from westagram.settings     import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        data                = json.loads(request.body)
        hashed_password     = bcrypt.hashpw(data['password'].encode('UTF-8'), bcrypt.gensalt()).decode('utf-8')
        
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
            user     = User.objects.get(email=email)
            token    = jwt.encode({'user_id': user.id}, SECRET_KEY, algorithm='HS256')

            if not bcrypt.checkpw(password.encode('UTF-8'), user.password.encode('UTF-8')):
                return JsonResponse({"massage": "INVALID_USER"}, status=401)

            return JsonResponse({'message':'SUCCESS', 'token':token}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

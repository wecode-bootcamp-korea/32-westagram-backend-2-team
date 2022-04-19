import json

from django.http            import JsonResponse
from django.views           import View

from users.models           import User

from django.core.exceptions import ValidationError
from users.validators       import (
                                UserEmailValidation,
                                validate_password,
                            )


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            check = UserEmailValidation()

            check.regex(email)
            check.duplicated(email)

            validate_password(password)

            User.objects.create(
                name         = data['name'],
                email        = email,
                password     = password,
                phone_number = phone_number
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except ValidationError as error:
            return JsonResponse({'message' : error.message}, status=error.code)


class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({'message' : 'INVALID_USER'}, code=401)

            return JsonResponse({'message' : 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
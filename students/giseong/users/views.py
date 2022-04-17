import json

from django.http  import JsonResponse
from django.views import View

from users.models import User

from users.inspections import (
    email_validation,
    email_existence,
    password_validation
)
from users.exceptions import (
    EmailValidationError,
    EmailExistenceError,
    PasswordValidationError
)


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email_validation(data['email'])
            password_validation(data['password'])
            email_existence(data['email'])

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number']
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except EmailValidationError:
            return JsonResponse({'message' : 'INVALID_EMAIL'}, status=400)

        except PasswordValidationError:
            return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=400)

        except EmailExistenceError:
            return JsonResponse({'message' : 'EXIST_EMAIL'}, status=400)

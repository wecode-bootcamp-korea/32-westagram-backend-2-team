from django.shortcuts import render

import json

import re

from django.http  import JsonResponse

from django.views import View

from users.models import User

class UserSignUpView(View):
    def post(self, request):
        data      = json.loads(request.body)
        if not data['email'] or not data['password']:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        if re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data["email"]) == None:
            return JsonResponse({"message": "ERROR_EMAIL_NEED_@_AND_."}, status=400)

        if re.match(r"^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[$@$!%*#?&])[A-Za-z0-9$@$!%*#?&].{8,}$", data["password"]) == None:
            return JsonResponse({"message": "ERROR_PASSWORD_STATUS"}, status=400)
        User.objects.create(
            name            = data['name'], 
            email           = data['email'],
            password        = data['password'],
            phone_number    = data['phone_number'] 
            )
        return JsonResponse({"message": "SUCCESS"}, status=201)



from re                     import compile

from users.models           import User

from django.core.exceptions import ValidationError


def validate_email(email):
    pattern = compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    if not pattern.match(email):
        raise ValidationError('Invalid Email', code=400)


def validate_password(password):
    pattern = compile('^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$')

    if not pattern.search(password):
        raise ValidationError('Invalid Password', code=400)


def exist_email(email):
    users_DB = User.objects.all()
    email_exist = users_DB.filter(email=email).exists()

    if email_exist:
        raise ValidationError('Exist Email', code=400)


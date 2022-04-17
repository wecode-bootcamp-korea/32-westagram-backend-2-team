from re               import compile

from users.models     import User

from users.exceptions import (
    PasswordValidationError,
    EmailValidationError,
    EmailExistenceError
)

def email_validation(email):
    pattern = compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    if not pattern.match(email):
        raise EmailValidationError


def password_validation(password):
    pattern = compile('^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$')

    if not pattern.search(password):
        raise PasswordValidationError


def email_existence(email):
    users_DB = User.objects.all()
    email_exist = users_DB.filter(email=email).exists()

    if email_exist:
        raise EmailExistenceError


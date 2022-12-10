from errors import InvalidLogin, InvalidPassword, InvalidEmail, ValidationError
import string


class Validator:
    @staticmethod
    def validate(user_data: tuple) -> None:
        try:
            Validator.validate_login(user_data[0])
            Validator.validate_password(user_data[1])
            Validator.validate_email(user_data[2])
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise ValidationError

    @staticmethod
    def validate_login(login: str) -> bool:
        if len(login) >= 6:
            return True
        else:
            raise InvalidLogin

    @staticmethod
    def validate_password(password: str) -> bool:
        if (len(password) >= 8 and
                len([p for p in password if p in string.ascii_lowercase]) > 0 and
                len([p for p in password if p in string.ascii_uppercase]) > 0 and
                not password.isalnum()):
            return True
        else:
            raise InvalidPassword

    @staticmethod
    def validate_email(email: str) -> bool:
        if '@' in email and email[-3] == '.' and email[-2:].isalpha():
            return True
        else:
            raise InvalidEmail


if __name__ == '__main__':
    Validator.validate(('user_login', 'Some!Password', 'mail@mail.by'))
    Validator.validate(('login', 'Some!Password', 'mail@mail.by'))
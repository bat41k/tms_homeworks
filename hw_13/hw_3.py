import re


class Validator:

    @staticmethod
    def validate(user_data: tuple[str, str, str]) -> bool:
        if re.match(r'^[A-Za-z0-9]{6,10}$', user_data[0]) and\
           re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', user_data[1]) and\
           re.match(r'^[\w\.]+@([\w-]+\.)+[\w-]{2,}$', user_data[2]):
            return True
        else:
            return False


if __name__ == '__main__':
    print(Validator.validate(('username', 'Password1!', 'user@mail.ru')))
    print(Validator.validate(('name', 'Password1!', 'user@mail.ru')))
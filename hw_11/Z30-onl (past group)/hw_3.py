# Добавить в TechnicalStaff статичный метод get_info(employee), получающий данные от работника и если работник из того
# же департамента - выдавать приветствие.

from datetime import date


class Employee:
    def __init__(self, first_name: str, last_name: str, age: int, profession: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.department = None

    @property
    def onboarding_time(self) -> date:
        return date(2022, 1, 1)

    @property
    def info(self) -> dict:
        return {'fullname': f'{self.first_name} {self.last_name}',
                'age': self.age,
                'working_time': f'{str((date(2022, 2, 1) - self.onboarding_time).days)} days',
                'department': self.department}


class TechnicalStaff(Employee):

    def change_department(self, new_department) -> None:
        self.department = new_department

    @staticmethod
    def get_info(employee: Employee) -> None:
        if employee.department == 'SEO':
            print('Привет!')


Person = TechnicalStaff(first_name='Aleksei', last_name='Podilo', age=33, profession='SEO Specialist')
Person.change_department('SEO')
TechnicalStaff.get_info(Person)
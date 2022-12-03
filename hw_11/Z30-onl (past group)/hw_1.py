# Создать класс Employee.
# Конструктор принимает first_name, last_name, age, profession.
# Person должен иметь свойство onboarding_time (выставляется по-умолчанию при создании объекта)
# Person должен иметь свойство info, возвращающее словарь
# {
# "fullname": полное_имя работника,
# "age": возраст работника,
# "working_time": количество времени, которое прошло с момента onboarding_time
# }

from datetime import date


class Employee:
    def __init__(self, first_name: str, last_name: str, age: int, profession: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    @property
    def onboarding_time(self) -> date:
        return date(2022, 1, 1)

    @property
    def info(self) -> dict:
        return {'fullname': f'{self.first_name} {self.last_name}',
                'age': self.age,
                'working_time': f'{str((date(2022, 2, 1) - self.onboarding_time).days)} days'}


Person = Employee(first_name='Aleksei', last_name='Podilo', age=33, profession='SEO Specialist')

assert Person.onboarding_time == date(2022, 1, 1)
assert Person.info == {'fullname': 'Aleksei Podilo',
                       'age': 33,
                       'working_time': '31 days'}
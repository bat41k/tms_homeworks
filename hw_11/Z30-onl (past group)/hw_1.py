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
        self._onboarding_time = date(2022, 1, 1)
        self.department = None

    @property
    def onboarding_time(self) -> date:
        return self._onboarding_time

    @onboarding_time.setter
    def onboarding_time(self, new_onboarding_time: date) -> None:
        self._onboarding_time = new_onboarding_time

    @property
    def info(self) -> dict:
        return {'fullname': f'{self.first_name} {self.last_name}',
                'age': self.age,
                'working_time': f'{str((date(2022, 2, 1) - self._onboarding_time).days)} days'}


Person = Employee(first_name='Aleksei', last_name='Podilo', age=33, profession='SEO Specialist')

if __name__ == '__main__':
    assert Person.onboarding_time == date(2022, 1, 1)
    assert Person.info == {'fullname': 'Aleksei Podilo',
                           'age': 33,
                           'working_time': '31 days'}
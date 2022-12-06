# Добавить в Employee атрибут класса department = None
# Унаследовать от Employee класс TechnicalStaff в котором реализовать метод класса change_department, позволяющий
# менять департамент
# Добавить в свойство info данные о департаменте

from hw_1 import Employee
from datetime import date


class TechnicalStaff(Employee):
    def __init__(self, first_name: str, last_name: str, age: int, profession: str) -> None:
        super().__init__(first_name, last_name, age, profession)

    @property
    def info(self) -> dict:
        return {'fullname': f'{self.first_name} {self.last_name}',
                'age': self.age,
                'working_time': f'{str((date(2022, 2, 1) - self.onboarding_time).days)} days',
                'department': self.department}

    def change_department(self, new_department: str) -> None:
        self.department = new_department


Person = TechnicalStaff(first_name='Aleksei', last_name='Podilo', age=33, profession='SEO Specialist')

if __name__ == '__main__':
    Person.change_department('SEO')
    assert Person.info == {'fullname': 'Aleksei Podilo',
                           'age': 33,
                           'working_time': '31 days',
                           'department': 'SEO'}
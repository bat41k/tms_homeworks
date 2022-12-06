# Добавить в TechnicalStaff статичный метод get_info(employee), получающий данные от работника и если работник из того
# же департамента - выдавать приветствие.

from hw_1 import Employee


class TechnicalStaff(Employee):
    def __init__(self, first_name: str, last_name: str, age: int, profession: str) -> None:
        super().__init__(first_name, last_name, age, profession)

    def change_department(self, new_department: str) -> None:
        self.department = new_department

    @staticmethod
    def get_info(employee: Employee) -> None:
        if employee.department == 'SEO':
            print('Hello!')


if __name__ == '__main__':
    Person = TechnicalStaff(first_name='Aleksei', last_name='Podilo', age=33, profession='SEO Specialist')
    Person.change_department('SEO')
    TechnicalStaff.get_info(Person)
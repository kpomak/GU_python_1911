"""
Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);

проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self):
        self.name = 'John'
        self.surname = 'Smith'
        self.position = 'developer'
        self._income = {'wage': 1000, 'bonus': 100}


class Position(Worker):
    def get_full_name(self):
        print(' '.join([self.name, self.surname]))

    def get_total_income(self):
        print(f'{self._income["wage"] + self._income["bonus"]} usd')


engineer = Position()
engineer.name = 'Tom'
engineer.surname = 'Li'
engineer.position = "teamlead"
engineer._income['wage'] = 2000
engineer._income['bonus'] = 200

print(engineer.name,
      engineer.surname,
      engineer.position,
      engineer._income['wage'],
      engineer._income['bonus'], sep='\n')

engineer.get_full_name()
engineer.get_total_income()

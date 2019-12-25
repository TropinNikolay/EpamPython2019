"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseCoffe(Component):
    def get_cost(self):
        return 90


class Marshmallow(Component):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 20


class Whip(Component):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 5


class Syrup(Component):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 15


if __name__ == "__main__":
    coffe = BaseCoffe()
    coffe = Whip(coffe)
    coffe = Marshmallow(coffe)
    coffe = Syrup(coffe)
    print("Итоговая стоимость за кофе: {}".format(str(coffe.get_cost())))

"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional

pancakes = {'eggs': 2, 'flour': 300, 'milk': 0.5, 'sugar': 100, 'sunflower_oil': 10, 'butter': 120}


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # handler1.set_next(handler2).set_next(handler3)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Fridge:
    def __init__(self, eggs, flour, milk, sugar, sunflower_oil, butter):
        self._eggs = eggs
        self._flour = flour
        self._milk = milk
        self._sugar = sugar
        self._sunflower_oil = sunflower_oil
        self._butter = butter


class EggsHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._eggs < pancakes['eggs']:
            print(f"Need to buy {pancakes['eggs'] - fridge._eggs} eggs")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class FlourHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._flour < pancakes['flour']:
            print(f"Need to buy {pancakes['flour'] - fridge._flour} flour")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class MilkHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._milk < pancakes['milk']:
            print(f"Need to buy {pancakes['milk'] - fridge._milk} milk")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class SugarHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._sugar < pancakes['sugar']:
            print(f"Need to buy {pancakes['sugar'] - fridge._sugar} sugar")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class SunflowerOilHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._sunflower_oil < pancakes['sunflower_oil']:
            print(f"Need to buy {pancakes['sunflower_oil'] - fridge._sunflower_oil} sunflower_oil")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class ButterHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._butter < pancakes['butter']:
            print(f"Need to buy {pancakes['butter'] - fridge._butter} butter")
        if self._next_handler:
            return self._next_handler.handle(fridge)


def get_missing_ingredients(fridge):
    eggs_handler = EggsHandler()
    flour_handler = FlourHandler()
    milk_handler = MilkHandler()
    sugar_handler = SugarHandler()
    sunflower_oil__handler = SunflowerOilHandler()
    butter_handler = ButterHandler()

    eggs_handler.set_next(flour_handler).set_next(milk_handler).set_next(sugar_handler).set_next(
        sunflower_oil__handler).set_next(butter_handler)

    eggs_handler.handle(fridge)


fridge_to_check = Fridge(eggs=1, flour=239, milk=0.2, sugar=10, sunflower_oil=0, butter=38)
get_missing_ingredients(fridge_to_check)

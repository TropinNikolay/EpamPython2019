"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""
from abc import ABC, abstractmethod
import yaml


class AbstractFirstCourse(ABC):
    @abstractmethod
    def get_first_course(self, menu) -> str:
        pass


class ConcreteFirstCourseChinese(AbstractFirstCourse):
    def get_first_course(self, menu) -> str:
        first_course = menu["first_courses"]["chinese"]
        return first_course


class ConcreteFirstCourseChild(AbstractFirstCourse):
    def get_first_course(self, menu) -> str:
        first_course = menu["first_courses"]["child"]
        return first_course


class ConcreteFirstCourseVegan(AbstractFirstCourse):
    def get_first_course(self, menu) -> str:
        first_course = menu["first_courses"]["vegan"]
        return first_course


class AbstractSecondCourse(ABC):
    @abstractmethod
    def get_second_course(self, menu) -> str:
        pass


class ConcreteSecondCourseChinese(AbstractSecondCourse):
    def get_second_course(self, menu) -> str:
        second_course = menu["second_courses"]["chinese"]
        return second_course


class ConcreteSecondCourseChild(AbstractSecondCourse):
    def get_second_course(self, menu) -> str:
        second_course = menu["second_courses"]["child"]
        return second_course


class ConcreteSecondCourseVegan(AbstractSecondCourse):
    def get_second_course(self, menu) -> str:
        second_course = menu["second_courses"]["vegan"]
        return second_course


class AbstractDrink(ABC):
    @abstractmethod
    def get_drink(self, menu) -> str:
        pass


class ConcreteDrinkChinese(AbstractDrink):
    def get_drink(self, menu) -> str:
        drink = menu["drinks"]["chinese"]
        return drink


class ConcreteDrinkChild(AbstractDrink):
    def get_drink(self, menu) -> str:
        drink = menu["drinks"]["child"]
        return drink


class ConcreteDrinkVegan(AbstractDrink):
    def get_drink(self, menu) -> str:
        drink = menu["drinks"]["vegan"]
        return drink


class AbstractFactory(ABC):
    @abstractmethod
    def create_first_course(self, menu):
        pass

    @abstractmethod
    def create_second_course(self, menu):
        pass

    @abstractmethod
    def create_drink(self, menu):
        pass


class ConcreteFactoryChinese(AbstractFactory):
    def create_first_course(self, menu) -> str:
        first_course = ConcreteFirstCourseChinese().get_first_course(menu)
        return first_course

    def create_second_course(self, menu) -> str:
        second_course = ConcreteSecondCourseChinese().get_second_course(menu)
        return second_course

    def create_drink(self, menu) -> str:
        drink = ConcreteDrinkChinese().get_drink(menu)
        return drink


class ConcreteFactoryChild(AbstractFactory):
    def create_first_course(self, menu) -> str:
        first_course = ConcreteFirstCourseChild().get_first_course(menu)
        return first_course

    def create_second_course(self, menu) -> str:
        second_course = ConcreteSecondCourseChild().get_second_course(menu)
        return second_course

    def create_drink(self, menu) -> str:
        drink = ConcreteDrinkChild().get_drink(menu)
        return drink


class ConcreteFactoryVegan(AbstractFactory):
    def create_first_course(self, menu) -> str:
        first_course = ConcreteFirstCourseVegan().get_first_course(menu)
        return first_course

    def create_second_course(self, menu) -> str:
        second_course = ConcreteSecondCourseVegan().get_second_course(menu)
        return second_course

    def create_drink(self, menu) -> str:
        drink = ConcreteDrinkVegan().get_drink(menu)
        return drink


def client_code(factory: AbstractFactory, day) -> None:
    with open('menu.yml', encoding='utf-8') as file:
        menu = yaml.load(file, Loader=yaml.FullLoader)

    menu = menu[day]
    first_course = factory.create_first_course(menu)
    second_course = factory.create_second_course(menu)
    drink = factory.create_drink(menu)
    print(f"{first_course}\n{second_course}\n{drink}")


if __name__ == "__main__":
    today = input("Please, input the day for your order: ")
    print()
    print(f"Vegan set lunch for {today}:")
    client_code(ConcreteFactoryVegan(), today)
    print("=" * 70)
    print(f"Child set lunch for {today}:")
    client_code(ConcreteFactoryChild(), today)
    print("=" * 70)
    print(f"Chinese set lunch for {today}:")
    client_code(ConcreteFactoryChinese(), today)
    print("=" * 70)

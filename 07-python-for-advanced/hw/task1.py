"""

Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:

* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса


>>> unit1 = SiamObj('1', '2', a=1)
>>> unit2 = SiamObj('1', '2', a=1)
>>> unit1 is unit2
True
>>> unit3 = SiamObj('2', '2', a=1)
>>> unit3.connect('1', '2', 1).a = 2
>>> unit2.a == 2
True
>>> pool = unit3.pool
>>> print(len(pool))
2
>>> del unit3
>>> print(len(pool))
1

"""
import weakref


def connect(cls, *args, **kwargs):
    hash = args + tuple(kwargs.values())
    for obj, code in cls._instances.items():
        if code == hash:
            return obj()
    else:
        print(f"Instance with attributes {hash} doesn't exist")


class Meta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instances = {}

    def __call__(cls, *args, **kwargs):
        def delete(instance):
            try:
                del cls._instances[weakref.ref(instance)]
            except KeyError:
                pass

        cls.connect = connect
        cls.pool = cls._instances
        cls.__del__ = delete

        instance = super().__call__(*args, **kwargs)
        hash = args + tuple(kwargs.values())
        for obj, code in cls._instances.items():
            if code == hash:
                return obj()
        else:
            cls._instances[weakref.ref(instance)] = hash
            return instance


class SiamObj(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        pass


class A(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        pass


class B(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        pass


unit1 = SiamObj("1", "2", a=1)
unit2 = SiamObj("1", "2", a=1)
print(unit1 is unit2)

unit3 = SiamObj("2", "2", a=1)
unit3.connect("1", "2", 1).a = 2
print(unit2.a == 2)

pool = unit3.pool
print(len(pool))

del unit3
print(len(pool))

"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""

import time
import uuid


def timer_property(t):
    class ModifiedProperty:
        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            self.__doc__ = doc
            self.set_time = None
            self.value = None

        def __get__(self, obj, objtype=None):
            """ Return an attribute of instance, which is of type owner. """
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("can't read attr")

            if not self.set_time or time.time() - self.set_time > t:
                self.value = self.fget(obj)
                self.set_time = time.time()
            return self.value

        def __set__(self, obj, value):
            """ Set an attribute of instance to value. """
            if self.fset is None:
                raise AttributeError("can't set attr")
            self.value = value

        def __delete__(self, obj):
            """ Delete an attribute of instance. """
            if self.fdel is None:
                raise AttributeError("can't del attr")
            self.fdel(obj)

        def getter(self, fget):
            """ Descriptor to change the getter on a property. """
            return self.__class__(fget, self.fset, self.fdel, self.__doc__)

        def setter(self, fset):
            """ Descriptor to change the setter on a property. """
            return self.__class__(self.fget, fset, self.fdel, self.__doc__)

        def deleter(self, fdel):
            """ Descriptor to change the deleter on a property. """
            return self.__class__(self.fget, self.fset, fdel, self.__doc__)

    return ModifiedProperty


class Message:
    @timer_property(t=1)
    def msg(self):
        self._msg = self.get_message()
        return self._msg

    @msg.setter  # reset timer also
    def msg(self, param):
        self._msg = param

    def get_message(self):
        """
        Return random string
        """
        return uuid.uuid4().hex


if __name__ == "__main__":
    m = Message()
    initial = m.msg
    assert initial is m.msg
    time.sleep(1)
    assert initial is not m.msg

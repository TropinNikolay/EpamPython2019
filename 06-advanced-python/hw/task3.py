""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    def __init__(self, *args, **kwargs):
        self.exceptions = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if issubclass(exc_type, self.exceptions):
            print('Suppressing', exc_val)
            return True


with Suppressor(ZeroDivisionError):
    1 / 0
print("It's fine")

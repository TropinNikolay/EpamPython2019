import time

from fib import fib

LOG_FIB_TUPLE = {'duration': 0, 'calls': 0}
LOG_FIB_RECURSION = {'duration': 0, 'calls': 0}
LOG_FIB_MATRIX = {'duration': 0, 'calls': 0}


def decorator_maker(log):
    def logging(function):
        is_evaluating = False

        def wrapper(*args, **kwargs):
            wrapper.count += 1
            nonlocal is_evaluating
            if is_evaluating:
                return function(*args, **kwargs)
            else:
                start_time = time.perf_counter()
                is_evaluating = True
                try:
                    value = function(*args, **kwargs)
                finally:
                    is_evaluating = False
                end_time = time.perf_counter()
                log['duration'] += float(format(end_time - start_time, '.5f'))
                log['calls'] = wrapper.count
                return value

        wrapper.count = 0
        return wrapper

    return logging


@decorator_maker(LOG_FIB_TUPLE)
def fib_tuple(n):
    assert n >= 0
    a, b = 0, 1
    if n == 1 or n == 0:
        return n
    else:
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


@decorator_maker(LOG_FIB_RECURSION)
def fib_recursion(n):
    assert n >= 0
    return n if n <= 1 else fib_recursion(n - 1) + fib_recursion(n - 2)


@decorator_maker(LOG_FIB_MATRIX)
def fib_matrix(n):
    return fib(n)


fib_tuple(100000)
print(LOG_FIB_TUPLE)
fib_tuple(100000)
print(LOG_FIB_TUPLE)

fib_recursion(20)
print(LOG_FIB_RECURSION)
fib_recursion(20)
print(LOG_FIB_RECURSION)

fib_matrix(100000)
print(LOG_FIB_MATRIX)
fib_matrix(100000)
print(LOG_FIB_MATRIX)

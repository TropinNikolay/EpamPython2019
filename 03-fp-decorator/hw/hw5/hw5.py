import time
import timeit
from functools import partial

import numpy as np
from matplotlib import pyplot

from fib import fib

LOG_FIB_TUPLE = {"duration": 0, "calls": 0}
LOG_FIB_RECURSION = {"duration": 0, "calls": 0}
LOG_FIB_MATRIX = {"duration": 0, "calls": 0}


def plot_time(func, inputs, repeats, n_tests):
    """
    Run timer and plot time complexity of `func` using the iterable `inputs`.
    Run the function `n_tests` times per `repeats`.
    """
    x, y, yerr = [], [], []
    for i in inputs:
        timer = timeit.Timer(partial(func, i))
        t = timer.repeat(repeat=repeats, number=n_tests)
        x.append(i)
        y.append(np.mean(t))
        yerr.append(np.std(t) / np.sqrt(len(t)))
    pyplot.errorbar(x, y, yerr=yerr, fmt="-o", label=func.__name__)


def plot_times(functions, inputs, repeats=3, n_tests=1, file_name=""):
    """
    Run timer and plot time complexity of all `functions`,
    using the iterable `inputs`.
    Run the functions `n_tests` times per `repeats`.
    Adds a legend containing the labels added by `plot_time`.
    """
    for func in functions:
        plot_time(func, inputs, repeats, n_tests)
    pyplot.legend()
    pyplot.xlabel("Input")
    pyplot.ylabel("Time [s]")
    if not file_name:
        pyplot.show()
    else:
        pyplot.savefig(file_name)


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
                log["duration"] += float(format(end_time - start_time, ".5f"))
                log["calls"] = wrapper.count
                return value

        wrapper.count = 0
        wrapper.__name__ = function.__name__
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

# uncomment to run comparison between fib_tuple and fib_matrix
# plot_times([fib_tuple, fib_matrix], np.linspace(1, 100000, num=50, dtype=int), repeats=10)

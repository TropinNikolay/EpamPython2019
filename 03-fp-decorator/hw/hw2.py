from functools import reduce


def is_armstrong(number):
    return reduce(lambda a, b: a + b, (int(ch) ** int(len(str(number))) for ch in str(number))) == number


assert is_armstrong(370) is True, 'Число Армстронга'
assert is_armstrong(153) is True, 'Число Армстронга'
assert is_armstrong(9) is True, 'Число Армстронга'
assert is_armstrong(10) is False, 'Не число Армстронга'

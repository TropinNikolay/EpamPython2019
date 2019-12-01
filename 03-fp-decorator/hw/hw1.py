"""
Problem 9
Special Pythagorean triplet
"""
print([int((lambda a, b: (a ** 2 + b ** 2) ** (1 / 2) * a * b)(a, b)) for a in range(1000) for b in range(1000) if a * b != 0 and (a ** 2 + b ** 2) ** (1 / 2) + a + b == 1000][0])

"""
Problem 6
Sum square difference
"""
print(sum(i for i in range(101)) ** 2 - sum(i * i for i in range(101)))

"""
Problem 48
Self powers
"""
print(sum(i ** i for i in range(1, 1001)) % 10 ** 10)

"""
Problem 40
Champernowne's constant
"""
from functools import reduce

print(reduce(lambda a, b: a * b, (int(''.join(str(i) for i in range(185186))[10 ** j]) for j in range(7))))

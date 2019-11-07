# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""


def is_permutation(a: str, b: str) -> bool:
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками

    if len(a) != len(b):
        return False

    marker = True
    for i in a:
        if a.count(i) != b.count(i):
            marker = False
    return marker


assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')

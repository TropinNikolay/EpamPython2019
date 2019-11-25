def letters_range(*args, **kwargs):
    def get_symbol(index):
        for key, value in alphabet.items():
            if value == index:
                if key in kwargs:
                    return str(kwargs[key])
                else:
                    return key

    alphabet = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }

    start = "a"
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    else:
        start, stop, step = args

    lst = []
    for i in range(alphabet[start], alphabet[stop], step):
        lst.append(get_symbol(i))

    return lst


print(letters_range("b", "w", 2))
print(letters_range("g"))
print(letters_range("g", "p"))
print(letters_range("g", "p", **{"l": 7, "o": 0}))
print(letters_range("p", "g", -2))
print(letters_range("a"))

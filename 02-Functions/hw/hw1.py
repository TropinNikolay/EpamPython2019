def letters_range(*args, **kwargs):
    def get_symbol(index):
        for key, value in alphabet.items():
            if value == index:
                if key in kwargs:
                    return str(kwargs[key])
                else:
                    return key

    alphabet = {(chr(ord("a") + i)): i for i in range(26)}
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

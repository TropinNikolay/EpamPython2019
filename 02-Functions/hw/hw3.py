def make_it_count(func, counter_name):
    def wrapped(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)

    return wrapped


def func(a=10, b=10):
    return a + b


x = 0
theta = make_it_count(func, "x")
print(theta(5, 6))
print(theta(15, 6))
print(theta(32, 6))
print(theta(87, 16))
print(theta(87, 16))
print(theta(87, 16))
print(x)

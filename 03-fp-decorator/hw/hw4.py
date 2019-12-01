def applydecorator(_):
    def say_my_name(function):
        def wrapper(*args, **kwargs):
            print(function.__name__)
            return function(*args, **kwargs)

        return wrapper

    return say_my_name


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))

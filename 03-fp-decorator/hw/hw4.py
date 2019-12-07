def applydecorator(function):
    def wrapper(foo):
        def inner(*args, **kwargs):
            return function(foo, *args, **kwargs)

        return inner

    return wrapper


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))

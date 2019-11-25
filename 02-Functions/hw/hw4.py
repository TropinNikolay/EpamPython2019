import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):
    def wrapped(*args, **kwargs):
        if args:
            list(fixated_args).extend(list(args))
        if kwargs:
            fixated_kwargs.update(kwargs)
        return func(*fixated_args, **fixated_kwargs)

    wrapped.__name__ = "func_{}".format(func.__name__)
    wrapped.__doc__ = """\
    A func implementation of {} with pre-applied arguments being: {} 
    source_code:\n{}""".format(wrapped.__name__, inspect.getcallargs(func), inspect.getsource(func))
    return wrapped


def example(a=10, b=10):
    return a + b


omega = modified_func(example, 4, 5)
print(omega.__name__)
print(omega())
print(omega.__doc__)

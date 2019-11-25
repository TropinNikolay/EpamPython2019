import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):
    def wrapped(*args, **kwargs):
        if fixated_args:
            list(args).extend(list(fixated_args))
        if fixated_kwargs:
            kwargs.update(fixated_kwargs)
        return func(*args, **kwargs)

    wrapped.__name__ = "func_{}".format(func.__name__)
    wrapped.__doc__ = """\
    A func implementation of {} with pre-applied arguments being: 
    fixated_args: {} fixated_kwargs: {} 
    source_code:\n{}""".format(wrapped.__name__, fixated_args, fixated_kwargs, inspect.getsource(func))
    return wrapped


def example(a=10, b=10):
    return a + b


omega = modified_func(example, 3, b=12)
print(omega.__name__)
print(omega(a=2, b=4))
print(omega.__doc__)

def atom(value=None):
    variable = value

    def get_value():
        nonlocal variable
        return variable

    def set_value(new_value):
        nonlocal variable
        variable = new_value
        return variable

    def process_value(*args):
        nonlocal variable
        for function in args:
            variable = function(variable)
        return variable

    def delete_value():
        nonlocal variable
        del variable

    return get_value, set_value, process_value, delete_value


vget, vset, veval, vdel = atom()
print(vget())
vset(10)
print(vget())
vset(15)
print(vget())
vdel()
vset(-100)
print(vget())
print(veval(abs, chr))

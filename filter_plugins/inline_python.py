#!/usr/bin/python3


def inline_python(*args, **kwargs):

    expression = args[0]

    monkey_patch = """
___print = print

global __inline_python_OUTPUT__
__inline_python_OUTPUT__ = ""

def print(line=""):
    global __inline_python_OUTPUT__
    __inline_python_OUTPUT__ = __inline_python_OUTPUT__ + "{0}\\n".format(line)

"""

    expression = monkey_patch + "\n" + expression

    globalz = globals()
    exec(expression, globalz, kwargs)

    return globalz['__inline_python_OUTPUT__']

def inline_python_func(*args, **kwargs):

    expression = args[0]

    monkey_patch = """

def __return_var(var_name):
    global __inline_python_RETURN_VAR__
    __inline_python_RETURN_VAR__ = var_name

"""

    expression = monkey_patch + "\n" + expression

    globalz = globals()
    exec(expression, globalz, kwargs)

    if '__inline_python_RETURN_VAR__' in globalz:
        return kwargs[globalz['__inline_python_RETURN_VAR__']]



class FilterModule(object):

    def filters(self):
        filter_list = {
            'inline_python': inline_python,
            'inline_python_func': inline_python_func
        }
        return filter_list

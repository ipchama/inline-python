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


class FilterModule(object):

    def filters(self):
        filter_list = {
            'inline_python': inline_python
        }
        return filter_list

__author__ = 'patrick'


class Macro(object):
    macros = {}

    def __init__(self, arguments):
        self.arguments = arguments

    def render(self):
        raise NotImplementedError("not implemented,please impplement in concrete class")

    @staticmethod
    def register(name):
        def decorator(cls):
            Macro.macros[name] = cls
            return cls

        return decorator

    @staticmethod
    def by_name(name):
        return Macro.macros.get(name)



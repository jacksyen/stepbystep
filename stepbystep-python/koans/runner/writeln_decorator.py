__author__ = 'patrick'


class WritelnDecorator:
    def __int__(self, stream):
        self.stream = stream

    def __getattr__(self, attr):
        return getattr(self.stream, attr)

    def writeln(self, arg=None):
        if arg: self.write(arg)
        self.write('\n')

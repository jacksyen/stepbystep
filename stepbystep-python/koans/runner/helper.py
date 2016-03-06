__author__ = 'patrick'


def class_name(obj):
    return obj.__class__.__name__


if __name__ == '__main__':
    print(class_name("test"))
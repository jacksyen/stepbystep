class Dog(object):
    def __init__(self):
        self.name = 'dog'
        print('Dog is created .....')

    def eat(self):
        print('eating .....')


class CrazyDog(Dog):
    def __init__(self):
        super().__init__()
        self.is_crazy = True

    def why_crazy(self):
        print('I am sick.......')

    def __getattr__(self, item):
        print('getting attribute', item)
        return (item, 'getattr_created')

    def __setattr__(self, key, value):
        print('using setattr set value')
        print(key, value)
        # super().__setattr__(key, value)
        setattr(self, key, value)


class Danger():
    def __int__(self):
        pass

    def hurt(self):
        print("hurt .....")

    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass


dog = Dog()
dog.eat()
print(dog.name)
print(Dog.__base__)
print(Dog.__bases__)

crazy_dog = CrazyDog()
crazy_dog.eat()
print(crazy_dog.name)
crazy_dog.why_crazy()
crazy_dog.name2 = 'test_set_attr'
print(crazy_dog.name1)
print(crazy_dog.name2)
# print(CrazyDog.__base__)
# print(CrazyDog.__bases__)

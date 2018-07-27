class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
             cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class BaseClass():
    name = 'Base'


class MyClass(BaseClass, metaclass=Singleton):
    pass


if __name__ == '__main__':
    myclass1 = MyClass().name
    print(myclass1.name)

    myclass2 = MyClass()
    print(myclass2.name)

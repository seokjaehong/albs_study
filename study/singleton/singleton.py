class Singleton(type):
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance


class MessageManager(metaclass=Singleton):
    print('ab')

a= MessageManager.instance('test')
# a = MessageManager()
print(a)
b = MessageManager.instance('test2')
print(b)

print(a == b)


class MessageManager2():
    def __init__(self,name):
        self.name=name

    @classmethod
    def foo(cls):
        return cls


a = MessageManager2('1')
# a = instance.foo()
print(a)
b = MessageManager2('1')

# b = instance2.foo()
print(b)
print(a == b)
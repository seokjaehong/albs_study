# #################################################
# class Person():
#     def __init__(self, name):
#         self.name = name
#
#     # def __init_subclass__(cls, **kwargs):
#     #     cls.name = kwargs['name'] + 'yah'
#
#     def say_hi(self):
#         print("Hello How are you?", self.name)
#
#
# p = Person('Baram')
# p.say_hi()
# #################################################

# #################################################

# class Robot:
#     population = 0  # 클래스 변수 ( 모든 인스턴스는 클래스변수를 읽고, 수정할 수 있다.)
#
#     def __init__(self, name):
#         self.name = name  # 객체 변수 (모든 인스턴스는 name이라는 변수를 갖게된다. 각각의 인스턴스들은 다른 인스턴스로 접근할 수 없다)
#         print('initialize:{}'.format(self.name))
#         Robot.population += 1
#
#     def die(self):
#         print("{}is being destroyed!".format(self.name))
#         Robot.population -= 1
#         if Robot.population == 0:
#             print("{} was last one".format(self.name))
#         else:
#             print("There are still {:d} robots working".format(Robot.population))
#
#     def say_hi(self):
#         print("greetings,my master call me {}".format(self.name))
#
#     @ classmethod
#     def how_many(cls):
#         print("we have {:d} robots".format(cls.population))
#
#
# r1 = Robot(name='Robot1')
# r1.say_hi()
# Robot.how_many()
#
# r2 = Robot(name='Robot2')
# r2.say_hi()
# Robot.how_many()
#
# r1.die()
# Robot.how_many()
# r2.die()
# Robot.how_many()
# #################################################


# class SchoolMember:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Initialize SchoolMember:{}'.format(self.name))
#
#     def tell(self):
#         print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=' ')
#
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('Initialize Teacher Member:{}'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('salary:{:d}'.format(self.salary))
#
#
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('Initialize Student Member:{}'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks:{}'.format(self.marks))
#
#
# t = list()
# t.append(Teacher('촘스키', 40, 31000))
# t.append(Teacher('펌킨', 44, 38000))
# t.append(Teacher('세이버', 41, 32000))
# t.append(Teacher('맥과이어', 54, 35000))
#
# s = list()
# s.append(Student('싸이', 25, 65))
# s.append(Student('홍길동', 26, 70))
# s.append(Student('타디스', 29, 85))
# print()
#
# members = t + s
# for member in members:
#     member.tell()
###################################################################

# class rec: pass
#
#
# rec.name = 'bob'
# rec.age = 40

# print(rec.name)
# x=rec()
# y=rec()
# print(x.name,y.name)

# x.name='sue'
#
# print(x.name,y.name,rec.name)
#
#
# print(list(rec.__dict__.keys()))
# print(list(name for name in rec.__dict__ if not name.startswith('__')))
#
# print(list(x.__dict__.keys()))
#
# print(list(y.__dict__.keys()))
#
# print(x.name, x.__dict__['name'])
# print(y.name)
# rec = ('Bob', 40.5, ['dev', 'mgr'])
# print(rec[0])
# rec={}
# rec

###################################################################

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s,%s]' % (self.name, self.pay)
    # def __str__(self):
    #     return '[Person: %s,%s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)

    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()

    # # print(bob.name, bob.pay)
    # # print(sue.name, sue.pay)
    # # print(bob.lastName(), sue.lastName())
    # print(bob)
    # print(sue)
    # sue.giveRaise(.10)
    # print(sue)
    #
    # tom.giveRaise(.10)
    # print(tom.lastName())
    # print(tom)

    # print('--All three--')
    # for obj in (bob, sue, tom):
    #     obj.giveRaise(.10)
    #     print(obj)

    # print(bob.name.split()[-1])
    # sue.pay *= 1.10
    # print('%.2f' % sue.pay)
    # name = 'Bob Smith'
    # name.split()
    # name.split()[-1]

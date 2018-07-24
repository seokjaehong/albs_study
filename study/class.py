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


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialize SchoolMember:{}'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialize Teacher Member:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary:{:d}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialize Student Member:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:{}'.format(self.marks))


t = list()
t.append(Teacher('촘스키', 40, 31000))
t.append(Teacher('펌킨', 44, 38000))
t.append(Teacher('세이버', 41, 32000))
t.append(Teacher('맥과이어', 54, 35000))

s = list()
s.append(Student('싸이', 25, 65))
s.append(Student('홍길동', 26, 70))
s.append(Student('타디스', 29, 85))
print()

members = t + s
for member in members:
    member.tell()

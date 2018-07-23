# import csv
#
#
# #
# # f = open('../csv_files/hotels.csv', 'r', encoding='utf-8')
# #
# # rdr = csv.reader(f)
# #
# # for line in rdr:
# #     # for r in line:
# #     print(line)
# # f.close()
class Person():
    def __init__(self, name):
        self.name = name

#
class EmailPerson(Person):
    def __init__(self, person, name, email):
        super(EmailPerson, self).__init__(name)
        self.person = person
        self.email = email


class EmailPhonePerson(EmailPerson):
    def __init__(self, person, email_person, name, email, phone):
        super(EmailPhonePerson, self).__init__(person, name, email)
        self.email_person = email_person
        self.email = email
        self.phone = phone


if __name__ == '__main__':
    p1 = Person('hong')
    p2 = EmailPerson(p1, 'hong2', '2hsj2334@gmail.com')
    p3 = EmailPhonePerson(p1, p2, 'hong3', '3hsj2334@gmail.com', '010-3113-2042')

    print(p1.name)
    print(p2.name, p2.person.name)
    print(p3.name, p3.email_person.name, p3.email_person.person.name)


# class Grandparent(object):
#     def __init__(self, name):
#         self.name = name
#
#     def my_method(self):
#         print ("Grandparent")
#
# class Parent(Grandparent):
#     def __init__(self, email ):
#         self.email = email
#     def some_other_method(self):
#         print ("Parent")
#
# class Child(Parent):
#     def __init__(self, name):
#         super(Child, self).__init__(name)
#
#     def my_method(self):
#         print ("Hello Grandparent")
#         print(super(Child, self).name)
#
# gp = Grandparent("종민이할아버지")
#
#
# child = Child("종민이")
# child.my_method()
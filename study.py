# class Human():
#     '''인간'''
#
#     # person = Human()
#     # person.name = '석재'
#     # person.weight = '100kg'
#
#     def create(self, name, weight):
#         # person = Human()
#         self.name = name
#         self.weight = weight
#         return self
#
#     def eat(self):
#         self.weight += 1
#         print('{}가 먹어서{}kg이 되엇다'.format(self.name, self.weight))
#
#
# # Human.create
# person = Human()
# person.create('석재', 100)
# person.eat()
class Fish:
    def __init__(self, first_name,last_name,skeleton,eyelids):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
        # print(args)

        # self.first_name = args[0]
        # self.last_name = args[1]
        # self.skeleton = args[2]
        # self.eyelids = args[3]

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Trout(Fish):
    def __init__(self, *args, **kwargs):
        self.water = kwargs.get('water')
        super(Trout,self).__init__(args[0].first_name,args[0].last_name,args[0].skeleton,args[0].eyelids,)


fish = Fish('aaa', 'bbb', 'ccc', 'ddd')

terry = Trout(fish, water='eee')
print(terry.__dict__)
# terry.last_name='exid'
# Initialize first name
# terry.first_name = "Terry"
# print(terry.first_name)
# Use parent __init__() through super()
# print(terry.first_name + " " + terry.last_name)
# print(terry.eyelids)

# Use child __init__() override
# print(terry.water)

# Use parent swim() method
terry.swim()

# class Shark(Fish):
#     def __init__(self, first_name, last_name="Shark",
#                  skeleton="cartilage", eyelids=True):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.skeleton = skeleton
#         self.eyelids = eyelids
#
#     def swim_backwards(self):
#         print("The shark cannot swim backwards, but can sink backwards.")
#
# sammy = Shark("Sammy")
# print(sammy.first_name + " " + sammy.last_name)
# sammy.swim()
# sammy.swim_backwards()
# print(sammy.eyelids)
# print(sammy.skeleton)

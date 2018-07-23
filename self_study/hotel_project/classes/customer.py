class Customer():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_customer_information(self):
        print('고객이름: {}'.format(self.id,self.name))


class GeneralCustomer(Customer):
    def __init__(self, id, name, email):
        super(GeneralCustomer, self).__init__(id, name)
        self.email = email

    def show_customer_information(self):
        print('General Customer id :{} 이름: {}, email:{}'.format(self.id,self.name, self.email))


class VipCustomer(Customer):
    def __init__(self, id, name, car_number=None, breakfast=None):
        super(VipCustomer, self).__init__(id, name)
        self.car_number = car_number
        self.breakfast = breakfast

    def show_customer_information(self):
        print('VIP Customer id :{} 이름: {}, 추천조식:{}, 차량번호:{}'.format(self.id,self.name, self.breakfast, self.car_number))



class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_customer_information(self):
        print('고객이름: {}'.format(self.id, self.name))


class GeneralCustomer(Customer):
    def __init__(self, id, name, email):
        super(GeneralCustomer, self).__init__(id, name)
        self.email = email

    def show_customer_information(self):
        print(f'ID: {self.id:<2}| 고객명: {self.name:<12} | 메일주소: {self.email:>15}')


class VipCustomer(Customer):
    def __init__(self, id, name, car_number=None, breakfast=None):
        super(VipCustomer, self).__init__(id, name)
        self.car_number = car_number
        self.breakfast = breakfast

    def show_customer_information(self):
        print(
            f'ID: {self.id:<2}| 고객명: {self.name:<12} | 추천조식:{self.breakfast:<5}, 차량번호:{self.car_number}')

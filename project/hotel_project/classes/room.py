


class Room():
    def __init__(self, room_id, number, price, max_people):
        self.room_id = room_id
        self.number = number
        self.price = price
        self.max_people = max_people

    def show_room_information(self):
        print('room_id:{}, number:{}, price:{}, '
              'max_people:{}'.format(self.room_id, self.number, self.price,
                                     self.max_people))

    def order_clean_service(self):
        print('전체 방청소 서비스')


class GeneralRoom(Room):
    def __init__(self, room_id, number, price, max_people):
        super(GeneralRoom, self).__init__(room_id, number, price, max_people)
        self.breakfast = False


class SingleRoom(GeneralRoom):
    def __init__(self, room_id, number, price, max_people):
        super(SingleRoom, self).__init__(room_id, number, price, max_people)
        self.clean_service = False

    def show_room_information(self):
        clean_service = "가능" if self.clean_service == True else "불가"
        print(
            f'ID: {self.room_id:<2}| 방 번호:{self.number:>6}호|'
            f' 가격:{self.price:>8}원| 정원: {self.max_people:>2}명| 클리닝서비스:{clean_service :>5}|')


class DoubleRoom(GeneralRoom):
    def __init__(self, room_id, number, price, max_people):
        super(DoubleRoom, self).__init__(room_id, number, price, max_people)
        self.clean_service = True

    def order_clean_service(self):
        print('일반 방청소 서비스')

    def show_room_information(self):
        clean_service = "가능" if self.clean_service == True else "불가"
        print(
            f'ID: {self.room_id:<2}| 방 번호:{self.number:>6}호|'
            f' 가격:{self.price:>8}원| 정원: {self.max_people:>2}명| 클리닝서비스:{clean_service:>5}|')


class VipRoom(Room):
    def __init__(self, room_id, number, price, max_people, breakfast):
        super(VipRoom, self).__init__(room_id, number, price, max_people)
        self.breakfast = breakfast
        self.clean_service = True

    def order_breakfast(self):
        print('아침을 주문해주세요')

    def order_clean_service(self):
        print('vip방청소 서비스')

    def show_room_information(self):
        clean_service = "가능" if self.clean_service == True else "불가"
        print(
            f'ID: {self.room_id:<2}| 방 번호:{self.number:>6}호| 가격:{self.price:>8}원|'
            f' 정원: {self.max_people:>2}명| 클리닝서비스:{clean_service:>5}| 아침식사:{self.breakfast:<14}')

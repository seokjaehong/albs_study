class Room():
    def __init__(self, room_id, number, price, max_people, is_possible):
        self.room_id = room_id
        self.number = number
        self.price = price
        self.max_people = max_people
        self.is_possible = is_possible

    def show_room_information(self):
        print('room_id:{}, number:{}, price:{}, '
              'max_people:{},예약가능여부:{}'.format(self.room_id, self.number, self.price,
                                               self.max_people, self.is_possible))

    def order_clean_service(self):
        print('전체 방청소 서비스')


class GeneralRoom(Room):
    def __init__(self, room_id, number, price, max_people, is_possible):
        super(GeneralRoom, self).__init__(room_id, number, price, max_people, is_possible)
        self.breakfast = False


class SingleRoom(GeneralRoom):
    def __init__(self, room_id, number, price, max_people, is_possible):
        super(SingleRoom, self).__init__(room_id, number, price, max_people, is_possible)
        self.clean_service = False

    def show_room_information(self):
        print('room_id:{}, number:{}, price:{}, max_people:{},'
              'clean_service:불가,예약가능여부:{}'.format(self.room_id, self.number,
                                                  self.price, self.max_people,
                                                  self.is_possible))


class DoubleRoom(GeneralRoom):
    def __init__(self, room_id, number, price, max_people, is_possible):
        super(DoubleRoom, self).__init__(room_id, number, price, max_people, is_possible)
        self.clean_service = True

    def order_clean_service(self):
        print('일반 방청소 서비스')

    def show_room_information(self):
        print('room_id:{}, number:{}, price:{}, max_people:{},'
              'clean_service:가능,예약가능여부:{}'.format(self.room_id, self.number,
                                                  self.price, self.max_people,
                                                  self.is_possible))


class VipRoom(Room):
    def __init__(self, room_id, number, price, max_people, is_possible, breakfast):
        super(VipRoom, self).__init__(room_id, number, price, max_people, is_possible)
        self.breakfast = breakfast
        self.clean_service = True

    def order_breakfast(self):
        print('아침을 주문해주세요')

    def order_clean_service(self):
        print('vip방청소 서비스')

    def show_room_information(self):
        print(
            'room_id:{}, number:{}, price:{}, max_people:{},'
            'clean_service:가능,예약가능여부:{},아침메뉴:{}'.format(self.room_id, self.number,
                                                        self.price,
                                                        self.max_people,
                                                        self.is_possible,
                                                        self.breakfast))

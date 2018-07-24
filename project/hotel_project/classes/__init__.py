


#
# class Room():
#     def __init__(self, *args, **kwargs):
#         super(Room, self).__init__(*args, **kwargs)
#         self.room_id = kwargs.get('room_id')
#         self.number = kwargs.get('number')
#         self.price = kwargs.get('price')
#         self.room_type = kwargs.get('room_type')
#         self.is_possible_reservation = "true"
#         self.max_people = kwargs.get('max_people')
#         # print('room init 호출!')
#
#     def __str__(self):
#         return "{}type의 {}번 방의 가격은 {}입니다".format(self.room_type, self.number, self.price)

#
# class Reservation(Room, Customer):
#     def __init__(self, fr_date, to_date, reserve_people_cnt, **kwargs):
#         Room.__init__(self, **kwargs)
#         Customer.__init__(self, **kwargs)
#         self.fr_date = fr_date
#         self.to_date = to_date
#         self.reserve_people_cnt = reserve_people_cnt
#
#         print("{} ~ {}날짜에 예약이 {}님 이름으로 완료 되었습니다. ".format(fr_date, to_date, kwargs.get('customer_name')))

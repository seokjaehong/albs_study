import ast


class Reservation():
    def __init__(self, id, customer, room, fr_date, to_date):
        self.id = id
        self.customer = customer
        self.room = room
        self.fr_date = fr_date
        self.to_date = to_date

    def show_reservation_information(self):
        from_date = str(self.fr_date.date())
        to_date = str(self.to_date.date())
        room_dic = ast.literal_eval(self.room)
        customer_dic = ast.literal_eval(self.customer)

        print(
            f'|예약기간은: {from_date:<10} ~ {to_date:<10}입니다.|'
            f' 방 번호:{room_dic["number"]:>6}호| 고객명:{customer_dic["name"]}'
        )

    # @classmethod
    # def create_reservation(cls,manager):
    #     #step1.날짜받기
    #     print('---------1.예약하실 날짜를 입력해주세요 --------')
    #     # reserve_date = cls..get_fr_to_date()
    #
    #     print('---------2.고객님의 ID를 선택해주세요--------')
    #     # obj.show_list("customer")
    #     # customer_id = input()
    #     #
    #     # print('---------3.예약할 룸 ID를 선택해주세요--------')
    #     # obj.show_list("room")
    #     # room_id = input()
    #     # self.create_reservation_info(customer_id, room_id, reserve_date[0]['fr_date'], reserve_date[0]['to_date'])
    #
    #     print('예약완료')

    # def create_reservation_info(self, customer_id, room_id, fr_date, to_date):
    #     result = []
    #     for j in self.customer_data:
    #         if j.id == customer_id:
    #             result.append(j)
    #
    #     for i in self.room_data:
    #         if i.room_id == room_id:
    #             result.append(i)
    #
    #     # max_id 값 받아오기
    #     max_id_value = file_reader_get_max_id('../csv_files/reservation.csv', 'r', 'utf-8')
    #     reservation = Reservation(id=max_id_value + 1, customer=result[0], room=result[1], fr_date=fr_date,
    #                               to_date=to_date)
    #
    #     # 새로생성된 Reseravation 저장하기
    #     file_writer('../csv_files/reservation.csv', 'a', 'utf-8', reservation, max_id_value)

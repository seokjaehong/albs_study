from ..classes.reservation import Reservation
from ..utils import get_data, file_reader, file_writer, convert_input_datetime, \
    file_reader_get_max_id


class HotelManagement:
    def __init__(self):
        self.room_data = get_data("room")
        self.customer_data = get_data("customer")
        self.reservation_data = get_data("reservation")

    def select_menu(self):
        print('')
        print('+++++++++Hotel Management System++++++++++++')
        print('+++++++++Please Select Menu++++++++++++++++')
        print('1.방리스트보기')
        print('2.예약하기')
        print('3.예약확인하기')
        print('기타.밖으로 나가기 ')
        select = input()
        return select

    def show_list(self, data):
        if data == "room":
            for i in self.room_data:
                i.show_room_information()
        elif data == "customer":
            for i in self.customer_data:
                i.show_customer_information()
        elif data == "reservation":
            for i in self.reservation_data:
                i.show_reservation_information()

    def create_reservation_info(self, customer_id, room_id, fr_date, to_date):
        result = []
        for j in self.customer_data:
            if j.id == customer_id:
                result.append(j)

        for i in self.room_data:
            if i.room_id == room_id:
                result.append(i)

        # max_id 값 받아오기
        max_id_value = file_reader_get_max_id('../csv_files/reservation.csv', 'r', 'utf-8')
        reservation = Reservation(id=max_id_value + 1, customer=result[0], room=result[1], fr_date=fr_date,
                                  to_date=to_date)

        # 새로생성된 Reseravation 저장하기
        file_writer('../csv_files/reservation.csv', 'a', 'utf-8', reservation, max_id_value)

    # def room_state_update(self, room_id):
    #     r = open('../csv_files/room.csv', 'r', encoding='utf-8')
    #     room_lists = csv.reader(r)
    #
    #     f = open('../csv_files/room_new.csv', 'a', encoding='utf-8', newline='')
    #     wr = csv.writer(f)
    #
    #     for room in list(room_lists):
    #         if room[1] == room_id:
    #             room[5] = 'False'
    #         wr.writerow(room)
    #     f.close()
    #     shutil.copy('../csv_files/room_new.csv', '../csv_files/room.csv')
    def get_fr_to_date(self):
        result = []
        while True:
            try:
                print('시작날짜:YYYY-MM-DD 형식으로 입력해주세요')
                string_fr_date = input()
                fr_date = convert_input_datetime(string_fr_date)
                print('종료날짜:YYYY-MM-DD 형식으로 입력해주세요')
                string_to_date = input()
                to_date = convert_input_datetime(string_to_date)

            except ValueError:
                print('날짜형식에 맞춰서 입력해주세요')
                continue
            else:
                result.append(
                    {
                        'fr_date': fr_date,
                        'to_date': to_date
                    })
                break
        return result

    # def get_customer_name(self):
    #     result=""
    #     while True:
    #         try:
    #             customer_name=input()
    #             for customer in self.customer_data:
    #                 if customer_name not in self.customer_data:
    #                     exp
    def make_reservation(self):
        print('---------1.예약하실 날짜를 입력해주세요 --------')
        reserve_date = self.get_fr_to_date()

        print('---------2.고객님의 ID를 선택해주세요--------')
        self.show_list("customer")
        customer_id = input()

        print('---------3.예약할 룸 ID를 선택해주세요--------')
        self.show_list("room")
        room_id = input()
        self.create_reservation_info(customer_id, room_id, reserve_date[0]['fr_date'], reserve_date[0]['to_date'])

        print('예약완료')

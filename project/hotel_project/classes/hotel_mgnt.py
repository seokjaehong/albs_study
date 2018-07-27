import ast
from .file_handler import FileHandler
from .reservation import Reservation
from project.hotel_project.utils import get_fr_to_date


class Singleton():
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance


class HotelManagement(Singleton):
    def __init__(self):
        self.file_handler = FileHandler()

    def select_menu(self):
        print('')
        print('++++++++++++++++++Hotel Management System+++++++++++++++++')
        print('++++++++++++++++++Please Select Menu++++++++++++++++++++++')
        print('++++++++++++++++++1.방리스트보기+++++++++++++++++++++++++++++')
        print('++++++++++++++++++2.고객리스트보기++++++++++++++++++++++++++++')
        print('++++++++++++++++++3.예약리스트보기++++++++++++++++++++++++++++')
        print('++++++++++++++++++4.예약하기+++++++++++++++++++++++++++++++++')
        print('++++++++++++++++++기타.밖으로 나가기+++++++++++++++++++++++++++')
        select = input()
        return select

    def show_data_list(self, data):
        if data == "room":
            for room in self.file_handler.room_data:
                room.show_room_information()
        elif data == "customer":
            for customer in self.file_handler.customer_data:
                customer.show_customer_information()
        elif data == "reservation":
            for reservation in self.file_handler.reservation_data:
                reservation.show_reservation_information()

    def create_reservation(self):
        print('---------1.예약하실 날짜를 입력해주세요 --------')
        reserve_date = get_fr_to_date()

        print('---------2.고객님의 ID를 선택해주세요--------')
        self.show_data_list("customer")
        customer_id = input()

        print('---------3.예약할 룸 ID를 선택해주세요--------')
        self.show_data_list("room")

        room_id = input()
        print('---------4.예약을 시작합니다. --------')

        self.save_reservation_detail(customer_id, room_id,
                                     reserve_date[0]['fr_date'],
                                     reserve_date[0]['to_date'])
        print('---------5.예약이 완료되었습니다.--------')

    def save_reservation_detail(self, customer_id, room_id, fr_date, to_date):
        if self.file_handler.reservation_data:
            check_value = self.check_available_reservation(room_id, fr_date,to_date)
        else:
            check_value = True

        if check_value:
            result = []

            for customer in self.file_handler.customer_data:
                if customer.id == customer_id:
                    result.append(customer)

            for room in self.file_handler.room_data:
                if room.room_id == room_id:
                    result.append(room)

            max_id_value = self.file_handler.get_reservation_max_id()
            reservation = Reservation(id=max_id_value + 1, customer=result[0], room=result[1], fr_date=fr_date,
                                      to_date=to_date)

            self.file_handler.write_csv_file(reservation, max_id_value)

            print(f'{reservation.customer.name:<5}님이 {fr_date}~{to_date}까지 {reservation.room.number:<5}호에 예약을 하셨습니다')
        else:
            print('해당 기간에는 이미 예약이 되어있습니다.')

    def check_available_reservation(self, room_id, fr_date, to_date):
        for reservation in self.file_handler.reservation_data:
            room_dic = ast.literal_eval(reservation.room)
            if room_dic['room_id'] == room_id:
                if reservation.fr_date.date() < fr_date <= reservation.to_date.date():
                    return False
                elif reservation.fr_date.date() <= to_date < reservation.to_date.date():
                    return False
                else:
                    return True
        return True

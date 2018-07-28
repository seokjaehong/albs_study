import ast
from .file_handler import FileHandler
from .reservation import Reservation
from project.hotel_project.utils import get_fr_to_date, get_room_id


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
        fr_date = reserve_date['fr_date']
        to_date = reserve_date['to_date']

        print('---------2.고객님의 ID를 선택해주세요--------')
        self.show_data_list("customer")
        customer_id = input()

        print('---------3.예약할 룸 ID를 선택해주세요--------')
        room_id = self.get_room_id(fr_date, to_date)

        print('---------4.예약을 시작합니다. --------')
        self.save_reservation_detail(customer_id, room_id, fr_date, to_date)

        print('---------5.예약이 완료되었습니다.--------')

    def get_room_id(self, fr_date, to_date):
        check_value = True
        while check_value:
            reservable_room_list = self.show_available_room_list(fr_date, to_date)
            room_id = input()

            for room in reservable_room_list:
                if room.room_id == room_id:
                    check_value = False

            if not check_value:
                return room_id
            else:
                print('예약가능한 룸ID를 입력해주세요')

    def show_available_room_list(self, fr_date, to_date):

        reservable_room_list = self.file_handler.room_data
        reservation_list = self.file_handler.reservation_data

        for reservation in reservation_list:
            room_dic = ast.literal_eval(reservation.room)
            if reservation.fr_date.date() <= fr_date < reservation.to_date.date() or reservation.fr_date.date() > to_date >= reservation.to_date.date():
                for room in reservable_room_list:
                    if room.room_id == room_dic['room_id']:
                        reservable_room_list.remove(room)

        for room in reservable_room_list:
            room.show_room_information()
        return reservable_room_list

    def save_reservation_detail(self, customer_id, room_id, fr_date, to_date):
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

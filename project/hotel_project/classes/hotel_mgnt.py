import ast
import math

from project.hotel_project.classes.customer import GeneralCustomer, VipCustomer
from project.hotel_project.classes.room import SingleRoom, DoubleRoom, VipRoom
from .file_handler import FileHandler
from .reservation import Reservation
from project.hotel_project.utils import get_fr_to_date, is_valid_email


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


# class HotelManagement():
class HotelManagement(Singleton):

    def __init__(self):
        self.file_handler = FileHandler()

    def select_menu(self):
        print('')
        print('++++++++++++++++++ Hotel Management System+++++++++++++++++')
        print('++++++++++++++++++ Please Select Menu     +++++++++++++++++')
        print('++++++++++++++++++ 1.방리스트보기            +++++++++++++++++')
        print('++++++++++++++++++ 2.고객리스트보기           +++++++++++++++++')
        print('++++++++++++++++++ 3.예약리스트보기          ++++++++++++++++++')

        print('++++++++++++++++++ 4.예약하기              ++++++++++++++++++')
        print('++++++++++++++++++ 5.방 생성하기           +++++++++++++++++++')
        print('++++++++++++++++++ 6.고객 생성하기           ++++++++++++++++++')

        print('++++++++++++++++++ 7.예약취소하기            ++++++++++++++++++')
        print('++++++++++++++++++ 8.방 삭제하기            ++++++++++++++++++')
        print('++++++++++++++++++ 9.고객 삭제하기            ++++++++++++++++++')

        print('++++++++++++++++++ 기타.밖으로 나가기         ++++++++++++++++++')
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

    class RoomManagement:
        def __init__(self):
            self.file_handler = FileHandler()

        def create_room(self):
            room_number = self.get_room_number()
            room_price = self.get_room_price()
            room_type = self.get_room_type()
            room_max_people = self.get_room_max_people()
            room_additional_info = self.get_room_additional_info(room_type)

            result = []
            max_id_value = self.file_handler.get_max_id("room")
            if room_type == "1":
                result = SingleRoom(max_id_value + 1, room_number, room_price, room_max_people)
            elif room_type == "2":
                result = DoubleRoom(max_id_value + 1, room_number, room_price, room_max_people)
            elif room_type == "3":
                result = VipRoom(max_id_value + 1, room_number, room_price, room_max_people,
                                 room_additional_info['breakfast'])

            self.file_handler.write_csv_file(result, max_id_value, 'room', room_type)

        def get_room_number(self):
            check_value = True
            room_number_list = []
            for room in self.file_handler.room_data:
                room_number_list.append(room.number)
            while check_value:
                print('---------방 번호를 입력해주세요 --------')
                room_number = input()
                try:
                    int_room_number = int(room_number)
                    if room_number in room_number_list:
                        print('이미 존재하는 방 번호 입니다. 다른 번호를 입력해주세요.')
                        continue
                    if 5 > math.floor(math.log10(int_room_number)) >= 2:
                        return int_room_number
                    else:
                        print('방 번호는 3자리이상, 5자리 이하로 입력해주세요')
                except ValueError:
                    print('숫자를 입력해주세요')

        def get_room_price(self):
            check_value = True
            while check_value:
                print('---------방의 가격을 입력해주세요 --------')
                room_price = input()
                try:
                    int_room_price = int(room_price)
                    if int_room_price >= 10000:
                        return int_room_price
                    else:
                        print('방의 금액은 10000원 이상으로 입력해주세요.')
                except ValueError:
                    print('숫자를 입력해주세요')

        def get_room_max_people(self):
            check_value = True
            while check_value:
                print('---------방의 최대인원을 입력해주세요 --------')
                room_max_price = input()
                try:
                    int_room_number = int(room_max_price)
                    return int_room_number
                except ValueError:
                    print('숫자를 입력해주세요')

        def get_room_type(self):
            check_value = True
            while check_value:
                print('---------방의 타입을 선택해주세요 --------')
                print('---------1.싱글룸             --------')
                print('---------2.더블룸             --------')
                print('---------3.VIP              --------')
                customer_type = input()
                if customer_type in ['1', '2', '3']:
                    return customer_type
                else:
                    print('다른 값을 선택하셨습니다. 다시 선택해주세요.')

        def get_room_additional_info(self, room_type):
            if room_type == '3':
                print('---------아침식사를 입력해주세요 --------')
                breakfast = input()
            else:
                breakfast = None
            return {'breakfast': breakfast}

        def delete_room(self):
            check_value = True
            while check_value:
                print('삭제할 방 ID를 입력해주세요')
                HotelManagement().show_data_list("room")

                room_id = input()

                for room in self.file_handler.room_data:
                    if room.id == room_id:
                        self.file_handler.delete_csv_file(room_id, "room")
                        check_value = False
                if check_value:
                    print('삭제가능한 룸ID를 입력해주세요')
            print('-----------삭제완료-----------')

    class CustomerManagement:
        def __init__(self):
            self.file_handler = FileHandler()

        def create_customer(self):
            customer_name = self.get_customer_name()
            customer_type = self.get_customer_type()
            customer_additional_info = self.get_customer_additional_info(customer_type)
            max_id_value = self.file_handler.get_max_id("customer")
            result = []
            if customer_type == "1":
                result = GeneralCustomer(max_id_value + 1, customer_name, customer_additional_info)
            elif customer_type == "2":
                result = VipCustomer(max_id_value + 1, customer_name, customer_additional_info['customer_car_number'],
                                     customer_additional_info['customer_breakfast'])
            self.file_handler.write_csv_file(result, max_id_value, 'customer', customer_type)

        def get_customer_type(self):
            check_value = True
            while check_value:
                print('---------VIP고객 여부를 선택해주세요 --------')
                print('---------1.일반 ')
                print('---------2.VIP')
                customer_type = input()
                if customer_type == '1' or customer_type == '2':
                    return customer_type
                else:
                    print('다른 값을 선택하셨습니다. 다시 선택해주세요.')

        def get_customer_name(self):
            print('---------고객이름을 입력해주세요 --------')
            customer_name = input()
            return customer_name

        def get_customer_additional_info(self, customer_type):
            if customer_type == '1':
                check_value = True
                while check_value:
                    print('---------고객email을 입력해주세요 --------')
                    customer_email = input()
                    if is_valid_email(customer_email):
                        return customer_email
                    else:
                        print('email형식에 맞게 입력해주세요.( ex) hsj2334@gmail.com')

            else:
                print('---------고객의 차량번호를 입력해주세요 --------')
                customer_car_number = input()
                print('---------고객의 추천조식을 입력해주세요 --------')
                customer_breakfast = input()
                return {'customer_car_number': customer_car_number, 'customer_breakfast': customer_breakfast}

        def delete_customer(self):
            check_value = True
            while check_value:
                print('삭제할 고객 ID를 입력해주세요')
                HotelManagement().show_data_list("customer")

                customer_id = input()

                for customer in self.file_handler.customer_data:
                    if customer.id == customer_id:
                        self.file_handler.delete_csv_file(customer_id, "customer")
                        check_value = False
                if check_value:
                    print('삭제가능한 고객 ID를 입력해주세요')
            print('-----------삭제완료-----------')

    class ReservationManagement:
        def __init__(self):
            self.file_handler = FileHandler()

        def create_reservation(self):
            print('---------1.예약하실 날짜를 입력해주세요 --------')
            reserve_date = get_fr_to_date()
            fr_date = reserve_date['fr_date']
            to_date = reserve_date['to_date']

            print('---------2.고객님의 ID를 선택해주세요--------')
            customer_id = self.get_reservable_customer()

            print('---------3.예약할 룸 ID를 선택해주세요--------')
            room_id = self.get_reservable_room_id(fr_date, to_date)

            print('---------4.예약을 시작합니다. --------')
            self.create_reservation_detail(customer_id, room_id, fr_date, to_date)

            print('---------5.예약이 완료되었습니다.--------')

        def show_available_room_list(self, fr_date, to_date):

            reservable_room_list = self.file_handler.room_data
            reservation_list = self.file_handler.reservation_data

            for reservation in reservation_list:
                room_dic = ast.literal_eval(reservation.room)
                if reservation.fr_date.date() <= fr_date < reservation.to_date.date() or reservation.fr_date.date() > to_date >= reservation.to_date.date():
                    for room in reservable_room_list:
                        if room.id == room_dic['id']:
                            reservable_room_list.remove(room)

            for room in reservable_room_list:
                room.show_room_information()
            return reservable_room_list

        def create_reservation_detail(self, customer_id, room_id, fr_date, to_date):
            result = []

            for customer in self.file_handler.customer_data:
                if customer.id == customer_id:
                    result.append(customer)

            for room in self.file_handler.room_data:
                if room.id == room_id:
                    result.append(room)

            max_id_value = self.file_handler.get_max_id("reservation")
            reservation = Reservation(id=max_id_value + 1, customer=result[0], room=result[1], fr_date=fr_date,
                                      to_date=to_date)

            self.file_handler.write_csv_file(reservation, max_id_value, 'reservation')

            print(f'{reservation.customer.name:<5}님이 {fr_date}~{to_date}까지 {reservation.room.number:<5}호에 예약을 하셨습니다')

        def get_reservable_customer(self):
            check_value = True
            while check_value:
                HotelManagement().show_data_list("customer")
                customer_id = input()

                for customer in self.file_handler.customer_data:
                    if customer.id == customer_id:
                        return customer_id

                if check_value:
                    print('예약가능한 고객 ID를 입력해주세요')

        def get_reservable_room_id(self, fr_date, to_date):
            check_value = True
            while check_value:
                reservable_room_list = self.show_available_room_list(fr_date, to_date)
                room_id = input()

                for room in reservable_room_list:
                    if room.id == room_id:
                        return room_id

                if check_value:
                    print('예약가능한 룸ID를 입력해주세요')

        def get_reservation_id(self):
            check_value = True
            while check_value:
                print("취소하실 예약ID를 선택해주세요")
                for reservation in self.file_handler.reservation_data:
                    reservation.show_reservation_information()

                reservation_id = input()
                for reservation in self.file_handler.reservation_data:
                    if reservation.id == reservation_id:
                        return reservation_id
                if check_value:
                    print('취소가능한 예약ID를 입력해주세요')

        def cancle_reservation(self):
            reservation_cancle_id = self.get_reservation_id()
            self.file_handler.delete_csv_file(reservation_cancle_id, "reservation")
            print('예약이 성공적으로 취소되었습니다.')

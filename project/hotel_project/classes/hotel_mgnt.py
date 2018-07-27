import ast
import datetime

from .customer import GeneralCustomer, VipCustomer
from .file_handle import FileHandle
from .reservation import Reservation
from .room import SingleRoom, DoubleRoom, VipRoom
from .utils import get_fr_to_date


class HotelManagement(FileHandle):

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
        data_list = self.set_data_from_csv_file(data)

        for i in data_list:
            if data == "room":
                i.show_room_information()
            elif data == "customer":
                i.show_customer_information()
            elif data == "reservation":
                i.show_reservation_information()
            else:
                break

    def set_data_from_csv_file(self, choice):
        result = []
        if choice == "room":
            lists = list(self.file_reader('./csv_files/room.csv', 'r', 'utf-8'))
            for i in lists:
                if i[0] == 'single':
                    result.append(SingleRoom(i[1], i[2], i[3], i[4]))
                elif i[0] == 'double':
                    result.append(DoubleRoom(i[1], i[2], i[3], i[4]))
                else:
                    result.append(VipRoom(i[1], i[2], i[3], i[4], i[5]))

        elif choice == "customer":
            customer_csv_lists = list(self.file_reader('./csv_files/customer.csv', 'r', 'utf-8'))
            for i in customer_csv_lists:
                if i[0] == 'GeneralCustomer':
                    result.append(GeneralCustomer(i[1], i[2], i[3]))
                else:
                    result.append(VipCustomer(i[1], i[2], i[3], i[4]))

        else:
            reservation_lists = list(self.file_reader('./csv_files/reservation.csv', 'r', 'utf-8'))
            for i in reservation_lists:
                result.append(
                    Reservation(
                        i[0], i[1], i[2],
                        datetime.datetime.strptime(i[3], '%Y-%m-%d'),
                        datetime.datetime.strptime(i[4], '%Y-%m-%d')
                    )
                )
        return result

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
        if self.set_data_from_csv_file('reservation'):
            reservation_data = self.set_data_from_csv_file('reservation')
            check_value = self.check_reservation_available(reservation_data, room_id, fr_date, to_date)
        else:
            check_value = True

        if check_value:
            result = []
            max_id_value = self.file_reader_get_max_id('./csv_files/reservation.csv', 'r', 'utf-8')
            customer_data = self.set_data_from_csv_file('customer')
            room_data = self.set_data_from_csv_file('room')

            for j in customer_data:
                if j.id == customer_id:
                    result.append(j)

            for i in room_data:
                if i.room_id == room_id:
                    result.append(i)

            reservation = Reservation(id=max_id_value + 1, customer=result[0], room=result[1], fr_date=fr_date,
                                      to_date=to_date)
            self.file_writer('./csv_files/reservation.csv', 'a', 'utf-8', reservation, max_id_value)
            print(f'{reservation.customer.name:<5}님이 {fr_date}~{to_date}까지 {reservation.room.number:<5}호에 예약을 하셨습니다')
        else:
            print('해당 기간에는 이미 예약이 되어있습니다.')

    def check_reservation_available(self, reservation_data, room_id, fr_date, to_date):
        for i in reservation_data:
            room_dic = ast.literal_eval(i.room)
            if room_dic['room_id'] == room_id:
                if i.fr_date.date() < fr_date <= i.to_date.date():
                    return False
                elif i.fr_date.date() <= to_date < i.to_date.date():
                    return False
                else:
                    return True
        return False

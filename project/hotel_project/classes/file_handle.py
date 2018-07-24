import csv
import datetime

from .customer import GeneralCustomer, VipCustomer
from .reservation import Reservation
from .room import SingleRoom, DoubleRoom, VipRoom


class FileHandle:
    __instance = None

    def __init__(self):
        self.room_data = self.get_data_from_csv_file('room')
        self.customer_data = self.get_data_from_csv_file('customer')
        self.reservation_data = self.get_data_from_csv_file('reservation_data')

    @classmethod
    def __getInstance(cls):
        return cls.__getInstance()

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__getInstance = cls(*args, **kwargs)
        cls.instance = cls.__getInstance
        return cls.__getInstance

    def get_fr_to_date(self):
        result = []
        while True:
            try:
                print('시작날짜: YYYY-MM-DD 형식으로 입력해주세요')
                string_fr_date = input()
                fr_date = self.convert_string_datetime(string_fr_date)
                print('종료날짜: YYYY-MM-DD 형식으로 입력해주세요')
                string_to_date = input()
                to_date = self.convert_string_datetime(string_to_date)

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

    def get_data_from_csv_file(self, choice):
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

    def show_data_list(self, data):
        for i in self.instance.get_data_from_csv_file(data):
            if data == "room":
                i.show_room_information()
            elif data == "customer":
                i.show_customer_information()
            elif data == "reservation":
                i.show_reservation_information()
            else:
                break

    def file_reader(self, file_name, read_select_type, encoding):
        r = open(file_name, read_select_type, encoding=encoding)
        rs = list(csv.reader(r))
        r.close()
        return rs

    def file_writer(self, file_name, read_select_type, encoding, obj, max_id_value):
        f = open(file_name, read_select_type, encoding=encoding, newline='')
        wr = csv.writer(f)
        wr.writerow([
            max_id_value + 1,
            obj.customer.__dict__,
            obj.room.__dict__,
            obj.fr_date,
            obj.to_date
        ])
        f.close()

    def file_reader_get_max_id(self, file_name, read_select_type, encoding):
        rs = self.file_reader(file_name, read_select_type, encoding)
        max_id_value = 0
        for i in rs:
            if int(i[0]) > max_id_value:
                max_id_value = int(i[0])
        return max_id_value

    def convert_string_datetime(self, str):
        year, month, day = map(int, str.split('-'))
        result = datetime.date(year, month, day)
        return result

    def create_reservation_info(self, customer_id, room_id, fr_date, to_date):
        result = []
        max_id_value = self.file_reader_get_max_id('./csv_files/reservation.csv', 'r', 'utf-8')

        for j in self.customer_data:
            if j.id == customer_id:
                result.append(j)

        for i in self.room_data:
            if i.room_id == room_id:
                result.append(i)
        reservation = Reservation(id=max_id_value + 1, customer=result[0], room=result[1], fr_date=fr_date,
                                  to_date=to_date)
        self.file_writer('./csv_files/reservation.csv', 'a', 'utf-8', reservation, max_id_value)
        print(f'{reservation.customer.name:<5}님이 {fr_date}~{to_date}까지 {reservation.room.number:<5}호에 예약을 하셨습니다')

    def create_booking(self):
        print('---------1.예약하실 날짜를 입력해주세요 --------')
        reserve_date = self.instance.get_fr_to_date()

        print('---------2.고객님의 ID를 선택해주세요--------')
        self.instance.show_data_list("customer")
        customer_id = input()

        print('---------3.예약할 룸 ID를 선택해주세요--------')
        self.instance.show_data_list("room")
        room_id = input()
        print('---------4.예약을 시작합니다. --------')

        self.instance.create_reservation_info(customer_id, room_id,
                                              reserve_date[0]['fr_date'],
                                              reserve_date[0]['to_date'])
        print('---------5.예약이 완료되었습니다.--------')

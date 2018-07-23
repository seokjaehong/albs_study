import csv
import shutil
from tempfile import NamedTemporaryFile

from self_study.hotel_project.classes.customer import GeneralCustomer, VipCustomer
from self_study.hotel_project.classes.reservation import Reservation
from self_study.hotel_project.classes.room import Room, SingleRoom, DoubleRoom, VipRoom


def get_data():
    room_data = []
    f = open('../csv_files/room.csv', 'r', encoding='utf-8')
    csv_lists = csv.reader(f)
    lists = list(csv_lists)
    for i in lists:
        if i[0] == 'single':
            room_data.append(SingleRoom(i[1], i[2], i[3], i[4], i[5]))
        elif i[0] == 'double':
            room_data.append(DoubleRoom(i[1], i[2], i[3], i[4], i[5]))
        else:
            room_data.append(VipRoom(i[1], i[2], i[3], i[4], i[5], i[6]))
    f.close()

    customer_data = []
    f = open('../csv_files/customer.csv', 'r', encoding='utf-8')
    csv_lists = csv.reader(f)
    lists = list(csv_lists)
    for i in lists:
        if i[0] == 'GeneralCustomer':
            customer_data.append(GeneralCustomer(i[1], i[2], i[3]))
        else:
            customer_data.append(VipCustomer(i[1], i[2], i[3], i[4]))
    f.close()

    reservation_data = []
    f = open('../csv_files/reservation.csv', 'r', encoding='utf-8')
    csv_lists = csv.reader(f)
    lists = list(csv_lists)
    for i in lists:
        reservation_data.append(Reservation(i[0], i[1], i[2], i[3]))
    f.close()

    return room_data, customer_data, reservation_data


class HotelManagement():

    def __init__(self):
        self.room_data = get_data()[0]
        self.customer_data = get_data()[1]
        self.reservation_data = get_data()[2]

    def select_menu(self):
        print('+++++++++Hotel Management System++++++++++++')
        print('+++++++++Please Select Menu++++++++++++++++')
        print('1.방리스트보기')
        print('2.예약하기')
        print('3.예약취소하기')
        print('4.밖으로 나가기 ')
        select = input()
        return select

    def show_room_list(self, is_possible=None):
        if is_possible:
            for i in self.room_data:
                if i.is_possible == "True":
                    i.show_room_information()
        else:
            for i in self.room_data:
                i.show_room_information()

    def show_customer_list(self):
        for i in self.customer_data:
            i.show_customer_information()

    def step_fr_to_date(self):
        print('시작날짜:YYYY-MM-DD 형식으로 입력해주세요')
        fr_date = input()

        print('종료날짜:YYYY-MM-DD 형식으로 입력해주세요')
        to_date = input()

        return [fr_date, to_date]

    def create_reservation_info(self, reservation):
        r = open('../csv_files/reservation.csv', 'r', encoding='utf-8')
        rs = list(csv.reader(r))
        max_id_value = 0
        for i in rs:
            if int(i[0]) > max_id_value:
                max_id_value = int(i[0])
        r.close()

        # 새로생성된 Reseravation 저장하기
        f = open('../csv_files/reservation.csv', 'a', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow([
            max_id_value + 1,
            reservation.room_id,
            reservation.customer_id,
            reservation.fr_date,
            reservation.to_date
        ])
        f.close()

    def room_state_update(self, room_id):
        r = open('../csv_files/room.csv', 'r', encoding='utf-8')
        room_lists = csv.reader(r)

        f = open('../csv_files/room_new.csv', 'a', encoding='utf-8', newline='')
        wr = csv.writer(f)

        for room in list(room_lists):
            if room[1] == room_id:
                room[5] = 'False'
            wr.writerow(room)
        f.close()
        shutil.copy('../csv_files/room_new.csv', '../csv_files/room.csv')

    def make_reservation(self):
        print('---------1.예약하실 날짜를 입력해주세요 --------')

        while True:
            try:
                reserve_date = self.step_fr_to_date()
            except ValueError:
                print('날짜형식에 맞춰서 입력해주세요')
                continue
            else:
                fr_date = reserve_date[0]
                to_date = reserve_date[1]
                break

        print('---------2.고객님의 ID를 선택해주세요--------')
        self.show_customer_list()
        customer_id = input()

        print('---------3.예약할 룸 ID를 선택해주세요--------')
        self.show_room_list(is_possible=True)
        room_id = input()

        # Reservation 데이터 생성하기
        reservation = Reservation(customer_id, room_id, fr_date, to_date)
        self.create_reservation_info(reservation)

        # Room status update 하기
        self.room_state_update(reservation.room_id)

    print('예약완료')


def cancle_reservation(self):
    print('---------고객님의 ID를 선택해주세요--------')
    self.show_customer_list()
    customer_id = input()

    reservation_list = self.reservation_data
    pass


if __name__ == '__main__':
    hotel = HotelManagement()

    select = hotel.select_menu()
    if select == '1':
        hotel.show_room_list()
    elif select == '2':
        hotel.make_reservation()
    elif select == '3':
        hotel.cancle_reservation()
    elif select == '4':
        exit()

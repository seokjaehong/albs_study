import csv
import datetime

from project.hotel_project.classes.customer import GeneralCustomer, VipCustomer
from project.hotel_project.classes.reservation import Reservation
from project.hotel_project.classes.room import SingleRoom, DoubleRoom, VipRoom


class FileHandler:
    CSV_ROOM_FILE = './csv_files/room.csv'
    CSV_CUSTOMER_FILE = './csv_files/customer.csv'
    CSV_RESERVATION_FILE = './csv_files/reservation.csv'

    def __init__(self):

        self.room_data = list(self.read_csv_file(self.CSV_ROOM_FILE, 'utf-8', 'room'))
        self.customer_data = list(self.read_csv_file(self.CSV_CUSTOMER_FILE, 'utf-8', 'customer'))
        self.reservation_data = list(self.read_csv_file(self.CSV_RESERVATION_FILE, 'utf-8', 'reservation'))

    def read_csv_file(self, file_name, encoding, choice):
        r = open(file_name, 'r', encoding=encoding)
        data_list = list(csv.reader(r))
        result = []
        if choice == 'room':
            for room in data_list:
                if room[0] == 'single':
                    result.append(SingleRoom(room[1], room[2], room[3], room[4]))
                elif room[0] == 'double':
                    result.append(DoubleRoom(room[1], room[2], room[3], room[4]))
                else:
                    result.append(VipRoom(room[1], room[2], room[3], room[4], room[5]))
        elif choice == "customer":
            for i in data_list:
                if i[0] == 'GeneralCustomer':
                    result.append(GeneralCustomer(i[1], i[2], i[3]))
                else:
                    result.append(VipCustomer(i[1], i[2], i[3], i[4]))

        else:
            for i in data_list:
                result.append(Reservation(i[0], i[1], i[2], datetime.datetime.strptime(i[3], '%Y-%m-%d'),
                                          datetime.datetime.strptime(i[4], '%Y-%m-%d')))
        r.close()
        return result

    def write_csv_file(self, obj, max_id_value):
        f = open(self.CSV_RESERVATION_FILE, 'a', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow([
            max_id_value + 1,
            obj.customer.__dict__,
            obj.room.__dict__,
            obj.fr_date,
            obj.to_date
        ])
        f.close()

    def get_reservation_max_id(self):
        # reservation = self.read_csv_file(self.CSV_RESERVATION_FILE,'r','utf-8')
        max_id_value = 0
        for reservation in self.reservation_data:
            print(reservation.id)
            if int(reservation.id) > max_id_value:
                max_id_value = int(reservation.id)
        return max_id_value

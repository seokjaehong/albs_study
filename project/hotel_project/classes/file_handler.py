import csv
import datetime
import shutil

from project.hotel_project.classes.customer import GeneralCustomer, VipCustomer
from project.hotel_project.classes.reservation import Reservation
from project.hotel_project.classes.room import SingleRoom, DoubleRoom, VipRoom


class FileHandler:
    CSV_ROOM_FILE = './csv_files/room.csv'
    CSV_CUSTOMER_FILE = './csv_files/customer.csv'
    CSV_RESERVATION_FILE = './csv_files/reservation.csv'
    CSV_RESERVATION_TEMP_FILE = './temp_files/reservation_temp.csv'
    ENCODING = 'utf-8'

    def __init__(self):

        self.room_data = self.read_csv_file(self.CSV_ROOM_FILE, self.ENCODING)
        self.customer_data = self.read_csv_file(self.CSV_CUSTOMER_FILE, self.ENCODING)
        self.reservation_data = self.read_csv_file(self.CSV_RESERVATION_FILE, self.ENCODING)

    def read_csv_file(self, file_name, encoding):
        r = open(file_name, 'r', encoding=encoding)
        data_list = list(csv.reader(r))
        result = []
        for data in data_list:
            if data[0] == 'single':
                result.append(SingleRoom(data[1], data[2], data[3], data[4]))
            elif data[0] == 'double':
                result.append(DoubleRoom(data[1], data[2], data[3], data[4]))
            elif data[0] == 'VIP':
                result.append(VipRoom(data[1], data[2], data[3], data[4], data[5]))
            elif data[0] == 'GeneralCustomer':
                result.append(GeneralCustomer(data[1], data[2], data[3]))
            elif data[0] == 'VipCustomer':
                result.append(VipCustomer(data[1], data[2], data[3], data[4]))
            else:
                result.append(Reservation(data[0], data[1], data[2], datetime.datetime.strptime(data[3], '%Y-%m-%d'),
                                          datetime.datetime.strptime(data[4], '%Y-%m-%d')))
        r.close()
        return result

    def write_csv_file(self, obj, max_id_value, class_name, customer_type=None):

        if class_name == "reservation":
            f = open(self.CSV_RESERVATION_FILE, 'a', encoding=self.ENCODING, newline='')
            wr = csv.writer(f)
            wr.writerow([
                max_id_value + 1,
                obj.customer.__dict__,
                obj.room.__dict__,
                obj.fr_date,
                obj.to_date
            ])
            f.close()
        elif class_name == "customer":
            f = open(self.CSV_CUSTOMER_FILE, 'a', encoding=self.ENCODING, newline='')
            wr = csv.writer(f)
            if customer_type == '1':
                wr.writerow([
                    'GeneralCustomer', max_id_value + 1, obj.name, obj.email
                ])
            elif customer_type == '2':
                wr.writerow([
                    'VipCustomer', max_id_value + 1, obj.name, obj.car_number, obj.breakfast
                ])
            f.close()
        elif class_name == "room":
            f = open(self.CSV_ROOM_FILE, 'a', encoding=self.ENCODING, newline='')
            wr = csv.writer(f)
            if customer_type == '1':
                wr.writerow([
                    'single', max_id_value + 1, obj.number, obj.price, obj.max_people
                ])
            elif customer_type == '2':
                wr.writerow([
                    'double', max_id_value + 1, obj.number, obj.price, obj.max_people
                ])
            elif customer_type == '3':
                wr.writerow([
                    'VIP', max_id_value + 1, obj.number, obj.price, obj.max_people, obj.breakfast
                ])
            f.close()

    def get_max_id(self, class_name):
        max_id_value = 0
        data_list = []
        if class_name == "reservation":
            data_list = self.reservation_data
        elif class_name == "customer":
            data_list = self.customer_data
        elif class_name == "room":
            data_list = self.room_data

        for data in data_list:
            if int(data.id) > max_id_value:
                max_id_value = int(data.id)
        return max_id_value

    def cancle_reservation_csv_file(self, reservation_id):
        r = open(self.CSV_RESERVATION_FILE, 'r', encoding=self.ENCODING)
        reservation_list = csv.reader(r)
        f = open(self.CSV_RESERVATION_TEMP_FILE, 'a', encoding=self.ENCODING, newline='')
        temp_reservation_list = csv.writer(f)

        for reservation in reservation_list:
            if reservation[0] != reservation_id:
                temp_reservation_list.writerow(reservation)
        f.close()
        shutil.copy(self.CSV_RESERVATION_TEMP_FILE, self.CSV_RESERVATION_FILE)

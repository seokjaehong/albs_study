import csv
import datetime
import shutil

from project.hotel_project.classes.customer import GeneralCustomer, VipCustomer
from project.hotel_project.classes.reservation import Reservation
from project.hotel_project.classes.room import SingleRoom, DoubleRoom, VipRoom


class FileHandler:
    ENCODING = 'utf-8'

    def __init__(self, file_format):
        self.room_data = self.read_csv_file(file_format['room'], self.ENCODING)
        self.customer_data = self.read_csv_file(file_format['customer'], self.ENCODING)
        self.reservation_data = self.read_csv_file(file_format['reservation'], self.ENCODING)

    # def save(self, file):
    #     file.close()

    def read_csv_file(self, file_name, encoding):
        r = open(file_name, 'r', encoding=encoding)
        data_list = list(csv.reader(r))
        result = []
        for data in data_list:
            if data[0] == 'single':
                result.append(SingleRoom(data[1], data[2], int(data[3]), data[4]))
            elif data[0] == 'double':
                result.append(DoubleRoom(data[1], data[2], int(data[3]), data[4]))
            elif data[0] == 'VIP':
                result.append(VipRoom(data[1], data[2], int(data[3]), data[4], data[5]))
            elif data[0] == 'GeneralCustomer':
                result.append(GeneralCustomer(data[1], data[2], data[3]))
            elif data[0] == 'VipCustomer':
                result.append(VipCustomer(data[1], data[2], data[3], data[4]))
            else:
                result.append(Reservation(data[0], data[1], data[2], datetime.datetime.strptime(data[3], '%Y-%m-%d'),
                                          datetime.datetime.strptime(data[4], '%Y-%m-%d')))
        r.close()
        # self.save(r)
        return result

    def write_csv_file(self, result, max_id_value, class_name, file_format):
        if class_name == "reservation":
            f = open(file_format[class_name], 'a', encoding=self.ENCODING, newline='')
            wr = csv.writer(f)

            obj = Reservation(
                id=max_id_value + 1,
                customer=result['customer'],
                room=result['room'],
                fr_date=result['fr_date'],
                to_date=result['to_date']
            )
            wr.writerow([
                max_id_value + 1,
                obj.customer.__dict__,
                obj.room.__dict__,
                obj.fr_date,
                obj.to_date,
            ])
            print(f'{obj.customer.name:<5}님이 {obj.fr_date}~{obj.to_date}까지 {obj.room.number:<5}호에 예약을 하셨습니다')
            # self.save(f)
            f.close()
        elif class_name == "customer":
            f = open(file_format[class_name], 'a', encoding=self.ENCODING, newline='')
            wr = csv.writer(f)
            if result['customer_type'] == '1':
                obj = GeneralCustomer(max_id_value + 1, result['customer_name'],
                                      result['customer_additional_info']['customer_email'])
                wr.writerow([
                    'GeneralCustomer', max_id_value + 1, obj.name, obj.email
                ])
            elif result['customer_type'] == '2':
                obj = VipCustomer(
                    max_id_value + 1,
                    result['customer_name'],
                    result['customer_additional_info']['customer_car_number'],
                    result['customer_additional_info']['customer_breakfast'])
                wr.writerow([
                    'VipCustomer', max_id_value + 1, obj.name, obj.car_number, obj.breakfast
                ])
            # self.save(f)
            f.close()

        elif class_name == "room":
            f = open(file_format[class_name], 'a', encoding=self.ENCODING, newline='')
            wr = csv.writer(f)
            if result['room_type'] == '1':
                obj = SingleRoom(max_id_value + 1, result['room_number'], result['room_price'],
                                 result['room_max_people'])
                wr.writerow([
                    'single', max_id_value + 1, obj.number, obj.price, obj.max_people
                ])

            elif result['room_type'] == '2':
                obj = DoubleRoom(max_id_value + 1, result['room_number'], result['room_price'],
                                 result['room_max_people'])
                wr.writerow([
                    'double', max_id_value + 1, obj.number, obj.price, obj.max_people
                ])
            elif result['room_type'] == '3':
                obj = VipRoom(max_id_value + 1, result['room_number'], result['room_price'], result['room_max_people'],
                              result['room_breakfast'])
                wr.writerow([
                    'VIP', max_id_value + 1, obj.number, obj.price, obj.max_people, obj.breakfast
                ])
            # self.save(f)
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

    def delete_csv_file(self, id, class_name, file_format):
        __CSV_ROOM_TEMP_FILE = './temp_files/room_temp.csv'
        __CSV_CUSTOMER_TEMP_FILE = './temp_files/customer_temp.csv'
        __CSV_RESERVATION_TEMP_FILE = './temp_files/reservation_temp.csv'

        origin_file = []
        temp_file = []
        if class_name == "reservation":
            origin_file = file_format[class_name]
            temp_file = __CSV_RESERVATION_TEMP_FILE
        elif class_name == "room":
            origin_file = file_format[class_name]
            temp_file = __CSV_ROOM_TEMP_FILE
        elif class_name == "customer":
            origin_file = file_format[class_name]
            temp_file = __CSV_CUSTOMER_TEMP_FILE

        r = open(origin_file, 'r', encoding=self.ENCODING)
        data_list = csv.reader(r)
        f = open(temp_file, 'a', encoding=self.ENCODING, newline='')
        wr = csv.writer(f)

        for data in data_list:
            if class_name == "reservation":
                if data[0] != id:
                    wr.writerow(data)
            else:
                if data[1] != id:
                    wr.writerow(data)

        r.close()
        f.close()
        self.copy_temp_to_origin(temp_file, origin_file)

    def copy_temp_to_origin(self, temp, origin):
        shutil.copy(temp, origin)

        f = open(temp, 'w')
        f.truncate()

        f.close()

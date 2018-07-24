import csv
import datetime
import unicodedata

from .classes.customer import GeneralCustomer, VipCustomer
from .classes.reservation import Reservation
from .classes.room import SingleRoom, DoubleRoom, VipRoom


def get_data(type):
    if type == "room":
        room_data = []
        lists = list(file_reader('../csv_files/room.csv', 'r', 'utf-8'))
        for i in lists:
            if i[0] == 'single':
                room_data.append(SingleRoom(i[1], i[2], i[3], i[4], i[5]))
            elif i[0] == 'double':
                room_data.append(DoubleRoom(i[1], i[2], i[3], i[4], i[5]))
            else:
                room_data.append(VipRoom(i[1], i[2], i[3], i[4], i[5], i[6]))
        return room_data
    elif type == "customer":
        customer_data = []
        customer_csv_lists = list(file_reader('../csv_files/customer.csv', 'r', 'utf-8'))
        for i in customer_csv_lists:
            if i[0] == 'GeneralCustomer':
                customer_data.append(GeneralCustomer(i[1], i[2], i[3]))
            else:
                customer_data.append(VipCustomer(i[1], i[2], i[3], i[4]))
        return customer_data
    else:
        reservation_data = []
        reservation_lists = list(file_reader('../csv_files/reservation.csv', 'r', 'utf-8'))

        for i in reservation_lists:
            reservation_data.append(
                Reservation(
                    i[0], i[1], i[2],
                    datetime.datetime.strptime(i[3], '%Y-%m-%d'),
                    datetime.datetime.strptime(i[4], '%Y-%m-%d')
                )
            )
        return reservation_data


def file_reader(file_name, read_type, encoding):
    r = open(file_name, read_type, encoding=encoding)
    rs = list(csv.reader(r))
    r.close()
    return rs


def file_writer(file_name, read_type, encoding, obj, max_id_value):
    f = open(file_name, read_type, encoding=encoding, newline='')
    wr = csv.writer(f)
    wr.writerow([
        max_id_value + 1,
        obj.customer.__dict__,
        obj.room.__dict__,
        obj.fr_date,
        obj.to_date
    ])
    f.close()


def file_reader_get_max_id(file_name, read_type, encoding):
    rs = file_reader(file_name, read_type, encoding)
    max_id_value = 0
    for i in rs:
        if int(i[0]) > max_id_value:
            max_id_value = int(i[0])
    return max_id_value


def convert_input_datetime(str):
    year, month, day = map(int, str.split('-'))
    result = datetime.date(year, month, day)
    return result


import ast
import csv
import json


class Reservation:
    def __init__(self, id, customer, room, fr_date, to_date):
        self.id = id
        self.customer = customer
        self.room = room
        self.fr_date = fr_date
        self.to_date = to_date

    def show_reservation_information(self):
        from_date=str(self.fr_date.date())
        to_date=str(self.to_date.date())
        room_dic = ast.literal_eval(self.room)
        customer_dic = ast.literal_eval(self.customer)

        print(
            # f'ID: {self.room_id:<2}, 방 번호:{self.number:>6}호,'
            f'|예약기간은: {from_date:<10} ~ {to_date:<10}입니다.|'
            f' 방 번호:{room_dic["number"]:>6}호| 고객명:{customer_dic["name"]}'
        )

    # @classmethod
    # def check_availability(self, customer_id, room_id, fr_date, to_date):
    #     r = open('../csv_files/reservation.csv', 'r', encoding='utf-8')
    #     rs = list(csv.reader(r))
    #     result=[]
    #     for i in rs:
    #         if i[3] > fr_date and i[4]< to_date:
    #             result.append(i)
    #
    #     r.close()
    #     return result

    # if room_id not in self.room_id and customer_id not in self.customer_id:
    #     # reservation = Reservation(customer_id, room_id, fr_date, to_date)
    #     return True
    # else:
    #     return False
    #     print('해당 방에 이미 예약이 되어있습니다.')

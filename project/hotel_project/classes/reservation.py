import ast


class Reservation():
    def __init__(self, id, customer, room, fr_date, to_date):
        self.id = id
        self.customer = customer
        self.room = room
        self.fr_date = fr_date
        self.to_date = to_date

    def show_reservation_information(self):
        from_date = str(self.fr_date.date())
        to_date = str(self.to_date.date())
        room_dic = ast.literal_eval(self.room)
        customer_dic = ast.literal_eval(self.customer)

        print(
            f'| 고객명:{customer_dic["name"]:<4}|방 번호:{room_dic["number"]:>6}호|'
            f' 예약기간은: {from_date:<10} ~ {to_date:<10}입니다.|'
        )

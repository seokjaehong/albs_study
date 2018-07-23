class Reservation():
    def __init__(self, customer_id, room_id, fr_date, to_date):
        self.customer_id = customer_id
        self.room_id = room_id
        self.fr_date = fr_date
        self.to_date = to_date

    # def check_availability(self, customer_id, room_id, fr_date, to_date):
        # if room_id not in self.room_id and customer_id not in self.customer_id:
        #     # reservation = Reservation(customer_id, room_id, fr_date, to_date)
        #     return True
        # else:
        #     return False
            # print('해당 방에 이미 예약이 되어있습니다.')
    #
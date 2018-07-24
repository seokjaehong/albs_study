from .classes.hotel_mgnt import HotelManagement

if __name__ == '__main__':
    while True:
        hotel = HotelManagement()
        select = hotel.select_menu()
        if select == '1':
            hotel.show_list("room")
        elif select == '2':
            hotel.make_reservation()
        elif select == '3':
            hotel.show_list("reservation")
        else:
            print("종료되었습니다.")
            exit()

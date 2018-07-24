from project.hotel_project.classes.hotel_mgnt import HotelManagement

if __name__ == '__main__':

    hotel = HotelManagement.instance()

    while True:
        select = hotel.select_menu()
        if select == '1':
            hotel.show_data_list("room")
        elif select == '2':
            hotel.show_data_list("customer")
        elif select == '3':
            hotel.show_data_list("reservation")
        elif select == '4':
            hotel.create_booking()
        else:
            print("종료되었습니다.")
            exit()

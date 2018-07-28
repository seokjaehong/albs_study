from project.hotel_project.classes.hotel_mgnt import HotelManagement

if __name__ == '__main__':
    hotel_manager = HotelManagement.instance()
    room_manager = hotel_manager.RoomManagement()
    customer_manager = hotel_manager.CustomerManagement()
    reservation_manager = hotel_manager.ReservationManagement()

    while True:

        select = hotel_manager.select_menu()
        if select == '1':
            hotel_manager.show_data_list("room")
        elif select == '2':
            hotel_manager.show_data_list("customer")
        elif select == '3':
            hotel_manager.show_data_list("reservation")
        elif select == '4':
            reservation_manager.create_reservation()
        elif select == '5':
            room_manager.create_room()
        elif select == '6':
            customer_manager.create_customer()
        elif select == '7':
            reservation_manager.cancle_reservation()
        elif select == '8':
            room_manager.delete_room()
        elif select == '9':
            customer_manager.delete_customer()
        else:
            print("종료되었습니다.")
            exit()

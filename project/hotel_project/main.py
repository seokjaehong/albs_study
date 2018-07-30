from project.hotel_project.classes.hotel_mgnt import HotelManagement

if __name__ == '__main__':
    hotel_manager = HotelManagement.instance()

    while True:

        select = hotel_manager.select_menu()
        if select == '1':
            hotel_manager.room_manager.show_room_list()
        elif select == '2':
            hotel_manager.customer_manager.show_customer_list()
        elif select == '3':
            hotel_manager.reservation_manager.show_reservation_list()
        elif select == '4':
            hotel_manager.reservation_manager.create_reservation()
        elif select == '5':
            hotel_manager.room_manager.create_room()
        elif select == '6':
            hotel_manager.customer_manager.create_customer()
        elif select == '7':
            hotel_manager.reservation_manager.cancle_reservation()
        elif select == '8':
            hotel_manager.room_manager.delete_room()
        elif select == '9':
            hotel_manager.customer_manager.delete_customer()
        else:
            print("종료되었습니다.")
            exit()

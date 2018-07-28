from project.hotel_project.classes.hotel_mgnt import HotelManagement

if __name__ == '__main__':

    result = []
    while True:
        hotel_manager = HotelManagement.instance()
        # hotel_manager = HotelManagement()

        select = hotel_manager.select_menu()
        if select == '1':
            hotel_manager.show_data_list("room")
        elif select == '2':
            hotel_manager.show_data_list("customer")
        elif select == '3':
            hotel_manager.show_data_list("reservation")
        elif select == '4':
            hotel_manager.create_reservation()
        elif select == '5':
            hotel_manager.create_room()
        elif select == '6':
            hotel_manager.create_customer()
        elif select == '7':
            hotel_manager.cancle_reservation()
        else:
            print("종료되었습니다.")
            exit()

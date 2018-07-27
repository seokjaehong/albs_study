from project.hotel_project.classes.hotel_mgnt import HotelManagement

if __name__ == '__main__':

    hotel_manager = HotelManagement.instance()
    # hotel_manager2 = HotelManagement.instance()
    # print(hotel_manager==hotel_manager2)
    # print(hotel_manager is hotel_manager2)

    result = []
    while True:
        select = hotel_manager.select_menu()
        if select == '1':
            hotel_manager.show_data_list("room")
        elif select == '2':
            hotel_manager.show_data_list("customer")
        elif select == '3':
            hotel_manager.show_data_list("reservation")
        elif select == '4':
            hotel_manager.create_reservation()
        else:
            print("종료되었습니다.")
            exit()

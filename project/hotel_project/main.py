from project.hotel_project.classes.file_handle import FileHandle
from project.hotel_project.classes.hotel_mgnt import HotelManagement
from project.hotel_project.classes.reservation import Reservation

if __name__ == '__main__':

    hotel = HotelManagement.instance()

    while True:
        select = hotel.select_menu()
        if select == '1':
            hotel.show_list("room")
        elif select == '2':
            hotel.show_list("customer")
        elif select == '3':
            hotel.show_list("reservation")
        elif select == '4':
            hotel.create_reservation()
        else:
            print("종료되었습니다.")
            exit()

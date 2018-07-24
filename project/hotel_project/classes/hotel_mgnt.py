from project.hotel_project.classes.file_handle import FileHandle


class HotelManagement(FileHandle):
    def select_menu(self):
        print('')
        print('++++++++++++++++++Hotel Management System+++++++++++++++++')
        print('++++++++++++++++++Please Select Menu++++++++++++++++++++++')
        print('++++++++++++++++++1.방리스트보기+++++++++++++++++++++++++++++')
        print('++++++++++++++++++2.고객리스트보기++++++++++++++++++++++++++++')
        print('++++++++++++++++++3.예약리스트보기++++++++++++++++++++++++++++')
        print('++++++++++++++++++4.예약하기+++++++++++++++++++++++++++++++++')
        print('++++++++++++++++++기타.밖으로 나가기+++++++++++++++++++++++++++')
        select = input()
        return select

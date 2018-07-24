# import csv
# import datetime
# import json
#
# # from .classes.customer import
#
# def get_list(type, id=None):
#     result = []
#     if type == "hotel":
#         f = open('../csv_files/hotels.csv', 'r', encoding='utf-8')
#         lists = csv.reader(f)
#         for line in lists:
#             result.append(Hotel(id=line[0], name=line[1], location=line[2]))
#         f.close()
#     elif type == "room":
#         f = open('../csv_files/room.csv', 'r', encoding='utf-8')
#         lists = csv.reader(f)
#
#         for line in lists:
#             if id == line[0]:
#                 result.append(
#                     Room(id=line[0], name=line[1], location=line[2], room_id=line[3], number=line[4], price=line[6],
#                          room_type=line[5])
#                 )
#         f.close()
#     return result
#
#
# def convert_input_datetime(str):
#     year, month, day = map(int, str.split('-'))
#     result = datetime.date(year, month, day)
#     return result
#
#
# def step_one():
#     print('시작날짜:YYYY-MM-DD 형식으로 입력해주세요')
#     date_input = input()
#     fr_date = convert_input_datetime(date_input)
#
#     print('종료날짜:YYYY-MM-DD 형식으로 입력해주세요')
#     date_input = input()
#     to_date = convert_input_datetime(date_input)
#     return [fr_date, to_date]
#
#
# def main():
#     print('원하시는 서비스를 선택해주세요.')
#     print('1.예약하기, 2.예약현황')
#
#     select_num = input()
#
#     if select_num == '1':
#         print('---------1.예약하시려는 날짜와 사람수를 입력해주세요.--------')
#         while True:
#             try:
#                 reserve_date = step_one()
#             except ValueError:
#                 print('날짜형식에 맞춰서 입력해주세요')
#                 continue
#             else:
#                 fr_date = reserve_date[0]
#                 to_date = reserve_date[1]
#                 break
#
#         print('예약할 사람 수를 입력해주세요')
#         reserve_people_cnt = input()
#
#         print('---------2.해당 날짜 사이에 예약가능한 호텔 리스트입니다.--------')
#         hotel_list = get_list("hotel")
#
#         for hotel in hotel_list:
#             print(hotel.id, hotel.name, hotel.location)
#         print('Hotel ID를 선택해 주세요')
#         hotel_id = input()
#
#         select_hotel = ""
#         for hotel in hotel_list:
#             if hotel_id == hotel.id:
#                 select_hotel = hotel
#
#         print('---------3.선택하신 {}호텔의 예약가능한 방의 리스트입니다.--------'.format(select_hotel.name))
#
#         room_lists = get_list("room", hotel_id)
#         for room in room_lists:
#             print('ID:{}, ROOM_TYPE:{}, PRICE:{}'.format(room.room_id, room.room_type, room.price))
#
#         print('Room ID를 선택해주세요')
#         room_id = input()
#
#         select_room = ""
#         for room in room_lists:
#             if room_id == room.room_id:
#                 select_room = room
#
#         print('---------4.추가정보 입력입니다.--------')
#         print('예약자 이름을 입력해주세요')
#         customer_name = input()
#         customer = Customer(customer_name=customer_name)
#
#         reservation = Reservation(customer_name=customer.customer_name, id=select_hotel.id,
#                                   location=select_hotel.location,
#                                   name=select_hotel.name, room_id=select_room.id, room_type=select_room.room_type,
#                                   price=select_room.price, number=select_room.number, fr_date=fr_date, to_date=to_date,
#                                   reserve_people_cnt=reserve_people_cnt)
#
#         # Reservation의 ID 얻어내기
#         r = open('../csv_files/reservation.csv', 'r', encoding='utf-8')
#         rs = list(csv.reader(r))
#         max_id_value = 0
#         for i in rs:
#             if int(i[0]) > max_id_value:
#                 max_id_value = int(i[0])
#         r.close()
#
#         # 새로생성된 Reseravation 저장하기
#         f = open('../csv_files/reservation.csv', 'a', encoding='utf-8', newline='')
#         wr = csv.writer(f)
#         wr.writerow([max_id_value + 1, reservation.__dict__])
#         f.close()
#
#         print('예약완료')
#
#     elif select_num == '2':
#         # 예약현황조회
#         r = open('../csv_files/reservation.csv', 'r', encoding='utf-8')
#         lists = list(csv.reader(r))
#         result = []
#         for line in lists:
#             text = line[1].replace("'", '"').replace("datetime", '"datetime').replace('),', ')",').replace(')}',
#                                                                                                            ')"}').replace(
#                 'None', 'null')
#             print(text)
#             json_text = json.loads(text)
#             result.append(json_text)
#         # print(result)
#         for i in result:
#             # print(i['fr_date'][14:24])
#             # print(type(i['fr_date']))
#             print('{}님은 {}호텔 {}호에 {}일 ~ {}일까지 {}명 예약이 되어있습니다.'.format(
#                 i['customer_name'],
#                 i['name'],
#                 i['number'],
#                 i['fr_date'][14:24],
#                 i['to_date'][14:24],
#                 i['reserve_people_cnt']))
#         r.close()
#
#     else:
#         print('서비스를 준비중입니다.')
#
#
# if __name__ == '__main__':
#     main()


# def room_state_update(self, room_id):
#     r = open('../csv_files/room.csv', 'r', encoding='utf-8')
#     room_lists = csv.reader(r)
#
#     f = open('../csv_files/room_new.csv', 'a', encoding='utf-8', newline='')
#     wr = csv.writer(f)
#
#     for room in list(room_lists):
#         if room[1] == room_id:
#             room[5] = 'False'
#         wr.writerow(room)
#     f.close()
#     shutil.copy('../csv_files/room_new.csv', '../csv_files/room.csv')
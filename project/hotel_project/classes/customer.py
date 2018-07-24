# -*- coding: utf-8 -*-
import mojimoji
import unicodedata


class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_customer_information(self):
        print('고객이름: {}'.format(self.id, self.name))


class GeneralCustomer(Customer):
    def __init__(self, id, name, email):
        super(GeneralCustomer, self).__init__(id, name)
        self.email = email

    def preformat_cjk(self, string, width, align='<', fill=' '):
        count = (width - sum(1 + (unicodedata.east_asian_width(c) in "WF")
                             for c in string))
        # print("#count:", count)
        return {
            '>': lambda s: fill * count + s,
            '<': lambda s: s + fill * count,
            '^': lambda s: fill * (count / 2)
                           + s
                           + fill * (count / 2 + count % 2)
        }[align](string)

    # def convert_full_to_half_char(self, ch):
    #     codeval = ord(ch)
    #     if 0xFF00 <= codeval <= 0xFF5E:
    #         ascii = codeval - 0xFF00 + 0x20;
    #         return unichr(ascii)
    #     else:
    #         return ch
    #
    # def convert_full_to_half_string(self, line):
    #     output_list = [self.convert_full_to_half_char(x) for x in line]
    #     return ''.join(output_list)

    def show_customer_information(self):
        # print(f'{self.name:<20}'+'+')
        # print(f'{mojimoji.han_to_zen(self.name):<20}'+'+')
        # print(f'{self.preformat_cjk(self.name,20)}'+'+')

        # customer_name = self.convert_full_to_half_string(self.name)

        print(f'ID: {self.id:<2}| 고객명: {self.name:<12} | 메일주소: {self.email:>15}')
        # print(' id :{} 이름: {}, email:{}'.format(self.id,self.name, self.email))


class VipCustomer(Customer):
    def __init__(self, id, name, car_number=None, breakfast=None):
        super(VipCustomer, self).__init__(id, name)
        self.car_number = car_number
        self.breakfast = breakfast

    def show_customer_information(self):
        print(
            f'ID: {self.id:<2}, 고객명: {self.name:<12}| 추천조식:{self.breakfast:<5}, 차량번호:{self.car_number}')
        # print('VIP Customer id :{} 이름: {}, 추천조식:{}, 차량번호:{}'.format(self.id,self.name, self.breakfast, self.car_number))

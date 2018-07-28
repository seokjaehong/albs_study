import datetime


def convert_string_datetime(str):
    year, month, day = map(int, str.split('-'))
    result = datetime.date(year, month, day)
    return result


def get_fr_to_date():
    result = []
    while True:
        try:
            print('시작날짜: YYYY-MM-DD 형식으로 입력해주세요')
            string_fr_date = input()
            fr_date = convert_string_datetime(string_fr_date)
            print('종료날짜: YYYY-MM-DD 형식으로 입력해주세요')
            string_to_date = input()
            if string_to_date > string_fr_date:
                to_date = convert_string_datetime(string_to_date)
            else:
                raise Exception
        except ValueError:
            print('날짜형식에 맞춰서 입력해주세요')
            continue
        except Exception as to_data:
            print('체크아웃 날짜는 체크인 날짜보다 작을수 없습니다.')
            continue
        else:
            break
    return {
        'fr_date': fr_date,
        'to_date': to_date
    }

#
# 생활코딩
# 1. 객체지향프로그래밍
# 1.1 모듈?
#  프로그램을 만드는 과정에서 생기는 함수들을 정리하기 위한 수단( == 수납공간)
# 1.2 클래스/ 인스턴스
#  포유류(클래스) - 사람 (인스턴스)
#              - 개  (인스턴스)
#              - 고양이(인스턴스)
# object(클래스와 인스턴스가 있다라고 기억하자, 이해는 좀 더 천천히 )


# 2. OOP (Object Oriented Programming)

class Cal(object):
    _history = []

    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1 + self.v2
        Cal._history.append("add :%d+%d=%d" % (self.v1, self.v2, result))
        return result

    def substract(self):
        result = self.v1 - self.v2
        Cal._history.append('substrac: %d-%d=%d' % (self.v1, self.v2, result))
        return result

    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

    def info(self):
        return "Cal => v1: %d ,v2: %d " % (self.v1, self.v2)


class CalMultiply(Cal):

    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalMultiply => %s" % super().info()


class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1 / self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalDivide => %s" % super().info()


c1 = Cal(10, 10)
print(c1.add())
print(c1.substract())
c2 = Cal(30, 20)

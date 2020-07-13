# 대륙명과 국가 리스트로 한 대륙을 표현하는 Continent 클래스 구현
# 1번 문제의 Country 클래스 사용

from typing import List, Any
from prob14_1 import Country

class Continent():
    def __init__(self, name, lst: List[Country]):
        self.name = name
        self.country1 = lst[0]
        self.country2 = lst[1]
        self.country3 = lst[2]

    def __str__(self):
        return '''{}
{}
{}
{}
'''.format(self.name, self.country1.__str__(), self.country2.__str__(), self.country3.__str__())




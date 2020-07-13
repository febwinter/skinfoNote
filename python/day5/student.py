class Student():
    def __init__(self, name: str, kor: int, eng: int, mat: int)-> None:
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def calc_sum(self) -> int:
        return self.kor + self.eng + self.mat

    def calc_avg(self)-> int:
        return self.calc_sum() / 3

        
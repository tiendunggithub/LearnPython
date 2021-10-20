class Student:
    def printInfo(self):
        print(f"""Thông tin sinh viên:
        Họ tên: {self.ten}
        Tuổi: {self.tuoi}""")

st1 = Student()
st1.ten = "TienDung"
st1.tuoi = 2
st1.printInfo()

class Info:
    def __init__(self, name="", age=18):
        self.name = name
        self.age = age
    def printkq(self):
        print(f"{self.name}")
st2 = Info()
st2.name = "NAM"
st2.printkq()

# có giá trị trả về
class Info2:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def old(self):
        return 2021 - self.year

mycv = Info2(2018, "Dung", "Quảng BÌnh")
print("My cv {} year old".format(mycv.old()))
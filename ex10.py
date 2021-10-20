class Member:
    def __init__(self, name = "", age = 20):
        self.name = name
        self.age = age
    def printname(self):
        print(f"Tên: {self.name}")
        print(f"Tuổi: {self.age}")

class Admin(Member):
    def printquyen(self):
        print(f"Quyền: {self.quyen}")

ad = Admin("Dũng")
ad.printname()
ad.quyen = "admin"
ad.printquyen()
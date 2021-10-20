def luythua(n):
    x = lambda x: x **n
    return x
tinhmu = luythua(3)
print(tinhmu(10))

# x = lambda a: a + 10
# y = lambda a, b: a + b

# print(x(20))
# print(y(100,200))
# def kl2(name = "Oggy"):
#     print(f"hello, I'm {name}")
# kl2()
# kl2("mark")

# def kl1(ds):
#     for i in ds:
#         print("Alo! {}".format(i))
# ds=["Tom","Jack"]
# kl1(ds)

# def kl(**sinhvien):
#     print("-----------------------------------------")
#     if "hoten" in sinhvien.keys():
#         print("Họ tên: {}".format(sinhvien["hoten"]))
#     if "diachi" in sinhvien.keys():
#         print("Địa chỉ: {}".format(sinhvien["diachi"]))
#     if "namsinh" in sinhvien.keys():
#         print("Năm sinh: {}".format(sinhvien["namsinh"]))
#     print("-----------------------------------------")
# kl(hoten="thu", diachi="huế", namsinh="2002")

# def smile(*name):
#     print("Số lượng tham số: {}".format(len(name)))
#     for x in name:
#         print(f"Xin chào {x}")

# smile("Jungle")
# smile()
# smile("nam","007","wick")

# #hàm không có tham số
# def alo():
#     print("hello")
# alo()

# #hàm có tham số
# def name(name, age):
#     print("Xin chao, toi la: {} - {} tuoi".format(name, age))
# name("dungx", 18)
# name(age=18, name="dungx")


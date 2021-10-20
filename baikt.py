str= "Tien Dung", "Gia Huy" , "Cuong Tran" 
def nhap_data():
    global str
    while True:
        print('Nhập tên sinh viên cần thêm: ')
        tmp = input()
        if tmp == 'stop':
            break
        str.append(tmp)
def tim_sinhvien(name, str):
    result = -1
    for i in range(0, len(str)):
        if str[i] == name:
            result = i
            break
    return result
op = True
while op:
    print ("""
    0.Thoát Chương Trình
    1.Nhập Thông Tin Sinh Viên
    2.Xóa sinh viên
    3.Tìm kiếm sinh viên
    4.Hiển thị bảng sinh viên
    """)
    op=input("Chọn chức năng? \n ") 
    if op=="0": 
        print("\n Thoát Chương Trình") 
        break
    elif op=="1":
        print("\n********Nhập Thông Tin Sinh Viên********") 
        print("\n(Nhập stop để dừng)\n") 
        nhap_data()
        print("\n====================================")
    elif op=="2":
        print("\n********Xóa Sinh Viên********") 
        n = int(input("Nhập vị trí muốn xóa: "))
        str.pop(n) 
        print(str)
        print("\n====================================")
    elif op=="3":
        print("\nTìm kiếm sinh viên")
        print("\nNhập tên sinh viên muốn tìm: ")
        name = input() 
        index = tim_sinhvien(name, str)
        if (index == -1):
            print("Không tìm thấy sinh viên")
            print("\n====================================")
        else:
            print("\nSinh viên được tìm thấy tại vị trí ", index+1)
            print("\n====================================")
    elif op=="4":
        print("\n********Danh sách sinh viên********") 
        print(str)
        print("\n====================================")
    elif op !="":
        print("\n********Vui lòng nhập lại********") 
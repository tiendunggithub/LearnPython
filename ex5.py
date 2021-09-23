op = True
while op:
    print ("""
    0.Thoát Chương Trình
    1.Nhập Thông Tin Sinh Viên
    2.Sắp xếp sinh viên theo điểm
    3.Tìm kiếm sinh viên
    4.Hiển thị bảng sinh viên
    """)
    op=input("Chọn chức năng? \n ") 
    if op=="0": 
      print("\n Thoát Chương Trình") 
      break
    elif op=="1":
      print("\n Nhập Thông Tin Sinh Viên") 
    elif op=="2":
      print("\n Sắp xếp sinh viên theo điểm") 
    elif op=="3":
      print("\n Tìm kiếm sinh viên") 
    elif op=="4":
      print("\n Hiển thị bảng sinh viên") 
    elif op !="":
      print("\n vui lòng nhập lại") 
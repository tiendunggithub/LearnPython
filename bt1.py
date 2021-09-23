dslop = []
hoten = input("Nhập Họ Tên: ")
dslop.append(hoten)
hoten = input("Nhập Họ Tên: ")
dslop.append(hoten)
hoten = input("Nhập Họ Tên: ")
dslop.append(hoten)
hoten = input("Nhập Họ Tên: ")
dslop.append(hoten)

print(dslop)

vitri = int(input("Bạn muốn sửa vị trí mấy:"))
hoten = input("Nhập họ tên mới: ")
dslop[vitri] = hoten

print(dslop)
print(dslop.sort())
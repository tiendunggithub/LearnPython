dslop = ["Nam", "An", "Binh", "Dat", "Huy"]
diachi = list(("176 tran phu" , "23 bui thi xuan", "98 ba trieu"))

print(dslop)
print(diachi)

print("Ho ten: " + dslop[1] + " - Dia chi: " + diachi[1])
print("Ho ten: " + dslop[-1] + " - Dia chi: " + diachi[-1])
print(dslop[1:3])

#cập nhật list
dslop[1] = "Cuong"
print(dslop)
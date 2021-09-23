import math
a = float(input("Nhập  a = "))
b = float(input("Nhập  b = "))
c = float(input("Nhập  c = "))
if (a == 0):
    if (b == 0):
        print ("Phương trình vô nghiệm!")
    else:
        print ("Phương trình có một nghiệm: x = ", + (-c / b))
d = b * b - 4 * a * c
if (d > 0):
    x1 = (float)((-b + math.sqrt(d)) / (2 * a))
    x2 = (float)((-b - math.sqrt(d)) / (2 * a))
    print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
elif (d == 0):
    x1 = (-b / (2 * a))
    print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
else:
    print("Phương trình vô nghiệm!")
 




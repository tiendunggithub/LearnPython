n = int(input())

def is_abundant(n):
    if n > 0:
        s = []
        a = 0
        for i in range(1,n):
            if n % i == 0:
                s.append(i)
                a = sum(s)
        if a > n: 
            print("true")
        else:
            print("false")
is_abundant(n)
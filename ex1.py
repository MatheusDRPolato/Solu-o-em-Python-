b = 2 
c = 7 
d = 3
a = int(input("Digite a posição que você queira descobrir:"))

if a == 1: 
    print(b)
elif a == 2:
    print(b)
    print(c)
elif a == 3: 
    print(b)
    print(c)
    print(d)
elif a >= 4: 
    print(b)
    print(c)
    print(d)
    a -= 3 
    while a > 0: 
        if a <= 1: 
            b *= 2
            print(b)
            a -= 1 
        elif a <= 2: 
            b *= 2
            c *= 3
            print(b)
            print(c)
            a -= 2 
        elif a >= 3: 
            b *= 2
            c *= 3
            d *= 4
            print(b)
            print(c)
            print(d)
            a = a - 3 
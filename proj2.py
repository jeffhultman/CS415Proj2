

def makeSameSize(a,b):
    while (len(a) != len(b)):
        if (len(a) > len(b)):
            b.append(0)
        elif (len(a) < len(b)):
            a.append(0)
    return a,b

def karatSuba_Multi(a,b):
    a = str(a)
    b = str(b)
    a = a[::-1]
    b = b[::-1]
    c = []
    d = []
    for digit in a:
        c.append (int(digit))
    for digit in b:
        d.append (int(digit))
    c,d = makeSameSize(c,d)
    return c,d

def main():
    a = input("Enter a number: (max 1000) ")
    b = input("Enter a second number: (max 1000) ")
    print(karatSuba_Multi(a,b))

main()
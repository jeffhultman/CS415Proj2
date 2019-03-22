def makeSameSize(a,b):
    while (len(a) != len(b)):
        if (len(a) > len(b)):
            b.append(0)
        elif (len(a) < len(b)):
            a.append(0)
    return a,b

def formatNumbers(a,b):
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
    a,b = makeSameSize(c,d)
    # i = len(a) - 1
    # while a[i] == 0:
    #     del a[i]
    #     i -= 1
    # i = len(b) - 1
    # while b[i] == 0:
    #     del b[i]
    #     i -= 1
    a.reverse()
    b.reverse()
    a =(''.join(str(i) for i in a))
    b =(''.join(str(i) for i in b))

    return a,b

def karatSuba(aString,bString):
    aString = str(aString)
    bString = str(bString)
    a = int(aString)
    b = int(bString)  
    if (a < 10) | (b < 10):
        return a * b
  

    n = max(len(aString), len(bString))
    nBy2 = int(n/2)
    a_upper = int(aString[:nBy2])
    a_lower = int(aString[nBy2:])
    b_upper = int(bString[:nBy2])
    b_lower = int(bString[nBy2:])
    c = karatSuba(a_lower, b_lower)
    d = karatSuba((a_upper + a_lower), (b_upper + b_lower))
    e = karatSuba(a_upper, b_upper)

    return (e*10**(n)) + ((d-e-c)*10**(nBy2))+e


def main():
    a = input("Enter a number: (max 1000) ")
    b = input("Enter a second number: (max 1000) ")
    a,b = formatNumbers(a,b)
    val = karatSuba(a,b)
    print(val)

main()
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
    if (len(aString) < 2) | (len(bString) < 2):
        return a * b
  

    n = max(len(aString), len(bString))
    nBy2 = int(n/2)
    a_upper = aString[:nBy2]
    a_lower = aString[nBy2:]
    b_upper = bString[:nBy2]
    b_lower = bString[nBy2:]
    c = karatSuba(int(a_lower), int(b_lower))
    d = karatSuba((int(a_upper) + int(a_lower)), (int(b_upper) + int(b_lower)))
    e = karatSuba(int(a_upper), int(b_upper))

    return (e*10**(2*nBy2)) + ((d-e-c)*10**(nBy2)) + e

def main():
    a = input("Enter a number: (max 1000) ")
    b = input("Enter a second number: (max 1000) ")
    a,b = formatNumbers(a,b)
    val = karatSuba(a,b)
    print(val)

main()
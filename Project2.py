def makeNum(a):
    numString = ""
    for i in range(len(a)):
        numString += str(a[i])
    return int(numString)

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
    # a.reverse()
    # b.reverse()
    # a =(''.join(str(i) for i in a))
    # b =(''.join(str(i) for i in b))

    return a,b

def listAdd(a,b): # a and b are lists
    # a.reverse()
    # b.reverse()
    carry = 0
    sum = 0
    returnVal = [0] * (len(a) + 1)
    for i in range(len(a)):
        sum = a[i] + b[i] + carry + returnVal[i]
        if (sum > 9):
            sum -= 10
            carry = 1
            returnVal[i+1] = carry
            returnVal[i] = sum
            carry = 0
        else:
            carry = 0
            returnVal[i] = sum
    returnVal.reverse()

    for i in range(len(returnVal) - 1):
        if (returnVal[i] == 0):
            del returnVal[i]
        else:
            break
    return returnVal

def listSub(a,b): # a-b
    # print(a)
    # print(b)
    negative = 0
    returnVal = []
    if (a[len(a)-1] <= b[len(b)-1]):
        a,b = b,a
        negative = 1

    for i in range(len(a)):
        if ((a[i] - b[i]) < 0) and (i < len(a) - 1):
            a[i] += 10
            a[i+1] -= 1
            returnVal.append(a[i] - b[i])
        else:
            returnVal.append(a[i] - b[i])
    returnVal.reverse() 
    if len(returnVal) > 1:
        for i in range(len(returnVal)):
            if (returnVal[0] == 0) and len(returnVal) > 1:
                del returnVal[0]
            else:
                break
    if negative:
        returnVal[0] *= -1
    return returnVal

    

def karatSuba(a,b): # a and b are lists
    if (len(a) < 2) and (len(b) < 2):
        return a[0] * b[0]
    n = len(a)
    nBy2 = int(n/2)

    a_upper = a[:nBy2]
    a_lower = a[nBy2:]
    b_upper = b[:nBy2]
    b_lower = b[nBy2:]

    c = karatSuba(a_lower, b_lower)
    sumAUp_ALow = listAdd(a_upper, a_lower)
    sumBUp_BLow = listAdd(b_upper, b_lower)
    d = karatSuba(sumAUp_ALow, sumBUp_BLow)
    e = karatSuba(a_upper, b_upper) - d - c
    e = listSub(e,d)
    e = listSub(e,c)    
    print(c)
    print(d)
    print(e)

    return (e*10**(2*nBy2)) + ((d-e-c)*10**(nBy2)) + e


def main():
    a = input("Enter a number: (max 1000) ")
    b = input("Enter a second number: (max 1000) ")
    # print("ActualSub:", (int(a) - int(b)))
    a,b = formatNumbers(a,b)
    # print(a)
    # print(b)
    val = karatSuba(a,b)
    # val =(''.join(str(i) for i in val))
    # val = int(val)
    # val = listSub(a,b)
    val = makeNum(val)
    print("ListSub:  ", val)

main()
def makeNum(a):
    numString = ""
    for i in range(len(a)):
        numString += str(a[i])
    return int(numString)

# a and b are forward
def makeSameSize(a,b):
    while (len(a) != len(b)):
        if (len(a) > len(b)):
            b.insert(0, 0)
        elif (len(a) < len(b)):
            a.insert(0, 0)
    if (len(a) % 2):
        a.insert(0, 0)
        b.insert(0, 0)
    return a,b

# a and b are forward
def formatNumbers(a,b):
    a = str(a)
    b = str(b)
    c = []
    d = []
    for digit in a:
        c.append (int(digit))
    for digit in b:
        d.append (int(digit))
    a,b = makeSameSize(c,d)
    return a,b

def listAdd(a,b): # a and b are lists
    print('add operands', a, b)

    if (a[0] < 0):
        a[0] *= -1
        return listSub(b,a)
    if (b[0] < 0):
        b[0] *= -1
        return listSub(a,b)
    a, b = makeSameSize(a, b)
    carry = 0
    sum = 0
    returnVal = []
    for i in range(len(a) - 1, -1, -1):
        sum = a[i] + b[i] + carry
        if (sum > 9):
            sum -= 10
            carry = 1
            # returnVal[i+1] = carry
            returnVal.insert(0,sum)
            # returnVal[i] = sum

        else:
            carry = 0
            returnVal.insert(0,sum)
            # returnVal[i] = sum
    # returnVal.reverse()

    for i in range(len(returnVal)):
        if (returnVal[0] == 0) and len(returnVal) > 1:
            del returnVal[0]
        else:
            break
    print('add result', returnVal)
 
    return returnVal

def listSub(a,b): # a-b
    print('sub operands', a, b)
    # a.reverse()
    # b.reverse()
    if (a[0] < 0):
        a[0] *= -1
        temp = listAdd(b,a)
        temp[0] *= -1
        return temp
    if (b[0] < 0):
        b[0] *= -1
        temp = listAdd(a,b)
        temp[0] *= -1
        return temp
    negative = 0
    returnVal = []
    for i in range(len(a)):
        if (a[0] == 0) and len(a) > 1:
            del a[0]
        else:
            break
    for i in range(len(b)):
        if (b[0] == 0) and len(b) > 1:
            del b[0]
        else:
            break
    if (len(a) < len(b)):
        a,b = b,a
        negative = 1
    elif len(a) == len(b):
        for i in range(len(a)):
            if (a[i] < b[i]):
                a,b = b,a
                negative = 1
                # a[0] *= -1
            else:
                break
        
    a, b = makeSameSize(a, b)
   
    
    
    
        

    for i in range(len(a) - 1, -1, -1):
        if ((a[i] - b[i]) < 0) and (i > 0):
            a[i] += 10
            a[i - 1] -= 1
            returnVal.insert(0,a[i] - b[i])
        else:
            returnVal.insert(0,a[i] - b[i])
    # returnVal.reverse() 
    if len(returnVal) > 1:
        for i in range(len(returnVal)):
            if (returnVal[0] == 0) and len(returnVal) > 1:
                del returnVal[0]
            else:
                break
    if negative:
        returnVal[0] *= -1
    print('sub result', returnVal)
    return returnVal

# Input is forward
def karatSuba(a,b):
    if (len(a) < 2) and (len(b) < 2):
        temp = str(a[0] * b[0])
        result = []
        for i in range(len(temp)):
            result.append(int(temp[i]))
        return result
    a, b = makeSameSize(a, b)
    n = len(a)
    nBy2 = n//2

    a1 = a[:nBy2]
    a0 = a[nBy2:]
    b1 = b[:nBy2]
    b0 = b[nBy2:]

    c_2 = karatSuba(a1, b1)
    c_0 = karatSuba(a0, b0)
    c_1 = listSub(karatSuba(listAdd(a1, a0), listAdd(b1, b0)), listAdd(c_2, c_0))
    for i in range(n):
        c_2.append(0)
    for i in range(nBy2):
        c_1.append(0)

    return listAdd(listAdd(c_2, c_1), c_0)



def main():
    a = input("Enter a number: (max 1000) ")
    b = input("Enter a second number: (max 1000) ")

    print("sub:  ", int(a)-int(b))
    a,b = formatNumbers(a,b)
    val = karatSuba(a,b)
    # val = listSub(a,b)
    val = makeNum(val)
    print(val)

main()
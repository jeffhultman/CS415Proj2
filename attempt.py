def strToArr(value):
	return list(value)

def pad(a, b):
	while len(a) < len(b):
		a.insert(0, '0')
	while len(b) < len(a):
		b.insert(0, '0')
	if (len(a) % 2):
		a.insert(0, '0')
		b.insert(0, '0')
	return a, b

# Assumes the arrays are already padded and of equal length
def add(a, b):
	a, b = pad(a, b)
	carry = '0'
	result = []
	i = len(a) - 1
	while i >= 0:
		res = list(str(int(a[i]) + int(b[i]) + int(carry)))
		if (len(res) > 1):
			result.insert(0, res[1])
			carry = res[0]
		else:
			result.insert(0, res[0])
			carry = '0'
		i -= 1
	if (carry != '0'):
		result.insert(0, carry)
	return result

def sub(a, b):
	a, b = pad(a, b)
	result = []
	i = len(a) - 1
	while i >= 0:
		res = str(int(a[i]) - int(b[i]))
		result.insert(0, res)
		i -= 1
	return result

def karatsuba(a, b):
	print(a)
	print(b)
	if (len(a) == 1 & len(b) == 1):
		return list(str(int(a[0]) * int(b[0])))
	a, b = pad(a, b)
	mid = len(a) // 2
	a_1 = a[:mid]
	a_0 = a[mid:]
	b_1 = b[:mid]
	b_0 = b[mid:]

	c_2 = karatsuba(a_1, b_1)
	print('c0')
	c_0 = karatsuba(a_0, b_0)
	c_1 = sub(karatsuba(add(a_1, a_0), add(b_1, b_0)), add(c_2, c_0))
	for i in range(len(a)):
		c_2.append(0)
	for i in range(mid):
		c_1.append(0)

	return add(add(c_2, c_1), c_0)


def main():
	a = input("Enter the first value")
	b = input("Enter the second value")
	a = strToArr(a);
	b = strToArr(b)
	print(karatsuba(a, b))
main()
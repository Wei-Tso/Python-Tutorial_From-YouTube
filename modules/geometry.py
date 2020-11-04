# 在 geometry 模組中定義幾何運算功能

# 計算兩點間的距離
def distance(x1, y1, x2, y2):
	return ((x2-x1)**2 + (y2-y1)**2)**0.5

# 計算兩點線段的斜率
def slope(x1, y1, x2, y2):
	return (y2-y1) / (x2-x1)

# 計算平均值
def average(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return (sum / len(numbers))

# 加法
def add(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum

# 減法
def subtract(*numbers):
	numbersList = list(numbers)
	withoutN1List = numbersList[1:]

	n1 = int(numbersList[0])
	sum = 0
	for n in withoutN1List:
		sum = sum - n
	return (n1+sum)

# 乘法
def multiply(*numbers):
	basic = 1
	for n in numbers:
		basic = basic*n
	return basic

# 除法
def divide(*numbers):
	numbersList = list(numbers)
	withoutN1List = numbersList[1:]

	n1 = int(numbersList[0])

	basic = 1
	if n1 == 0:
		return 0
	else:
		for n in withoutN1List:
			if (0 in withoutN1List)==True:
				return "分母不能為 0"
			else:
				basic = basic * n
	return (n1/basic)
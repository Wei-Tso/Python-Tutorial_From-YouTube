# 預設資料
# 基本語法
'''
def 函式名稱(參數名稱=預設資料):
	函式內部的程式碼
'''

def say(msg = "Hello"):
	print(msg)
say()
say("Hello world")

def power(base , exp=0):
	print(base**exp)
power(2 , 3)
power(4)

#--------------------------------------------------------

# 名稱對應
# 基本語法
'''
def 函式名稱(名稱1 , 名稱2):
	函式內部的程式碼

函式名稱(名稱2 = 3 , 名稱1 = 5)
'''

def divide(n1 , n2):
	result = n1 / n2
	print(result)

divide(2 , 4)
divide(n2 = 2 , n1 = 4)

def divide(numerator , denominator):
	print(numerator / denominator)

divide(1 , 3)
divide(denominator = 5 , numerator = 2)


#--------------------------------------------------------

# 無限參數
# 基本語法
'''
def 函式名稱(*無限參數):	# * 號一定要加
	無限參數以 Tuple 資料形態處理
	函式內部的程式碼

函式名稱(資料一，資料二，資料三)
'''

def say(*msgs):
	for msg in msgs:
		print(msgs)

say("Hello" , "Arbitrary" , "Arguments")

def average(*numbers):
	# print(numbers)
	sum = 0
	for n in numbers:
		sum = sum + n
	print(sum / len(numbers))
	# average = sum / len(numbers)
	# print(average)
average(3, 4)
average(6, 8, -1)
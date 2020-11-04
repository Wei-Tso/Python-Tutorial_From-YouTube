# 函式：程式碼包裝在一個區塊中，方便隨時呼叫使用
# 要先定義(建立)函式，然後才能呼叫(使用)函式

# 定義函式
# 基本語法
# 參數名稱可以不用寫
'''
def 函式名稱(參數名稱):
	函式內部的程式碼
'''

def sayHello():
	print("Hello")

# 定義可以印出任何訊息的函式
def say(msg):
	print(msg)

# 定義一個可以做加法的函式
def add(n1 , n2):
	result = n1 + n2
	print(result)


#--------------------------------------------------------

# 呼叫函式
# 基本語法
'''
函式名稱(參數資料)
'''

#--------------------------------------------------------

# 回傳值
# 基本語法一
'''
def 函式名稱(參數名稱):
	函式內部的程式碼
	return	# 結束函式，回傳 None
'''
# 基本語法二
'''
def 函式名稱(參數名稱):
	函式內部的程式碼
	return 資料	# 結束函式，回傳 資料
'''

def say(msg):
	print(msg)
	return
value = say("Hello")
print(value)

def add(n1 , n2):
	result = n1 + n2
	return "Hello"
value = add(1 , 2)
print(value)

def add(n1 , n2):
	result = n1 + n2
	return result
value = add(1 , 2)
print(value)


#--------------------------------------------------------

def multiply(n1 , n2):
	# print(n1 * n2)
	return n1 * n2

# multiply(3 , 4)
# multiply(1.8 , 2.732)
print(multiply(1 , 3))
# print(value)

#--------------------------------------------------------

# 程式的包裝
# 同樣的邏輯可以重複利用
# 求 1+2+...+100 的總合
def calculate(n1 , n2):
	sum = 0
	for x in range(n1 , n2+1):
		sum = sum + x
	print(sum)
calculate(1 , 100)
calculate(5 , 10)
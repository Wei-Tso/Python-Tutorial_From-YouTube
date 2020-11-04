'''
類別的兩種方法
1. 類別與類別屬性
2. 類別與實體物件、實體屬性、實體方法
# 實體屬性 與 Lecture 16 中的 類別屬性 為不同的概念
# 實體屬性 屬於 建立好的實體物件，放在變數中
'''

# 實體物件
# 透過類別建立
# 先定義類別，再透過類別建立實體物件
# 要先建立實體物件，然後才能使用實體屬性

# 建立實體
# 基本語法
'''
class 類別名稱:
	# 定義初始化函式
	def __init__(self):
		透過操作 self 來定義實體屬性

# 建立實體物件，放入變數 obj 中
obj = 類別名稱()	# 呼叫初始化函式
'''

#----------------------------Example----------------------------

class Point:
	def __init__(self):
		self.x = 3
		self.y = 4

# 建立實體物件
# 此實體物件包含 x 和 y 兩個實體屬性
p = Point()

#----------------------------Example----------------------------

class Point:
	def __init__(self , x , y):
		self.x = x
		self.y = y

# 建立實體物件
# 此實體物件包含 x 和 y 兩個實體屬性
# 建立時，可直接傳入參數資料
p = Point(1,5)

#--------------------------------------------------------

# 使用實體物件
# 基本語法
'''
實體物件.實體屬性名稱
'''

#----------------------------Example----------------------------

class Point:
	def __init__(self , x , y):
		self.x = x
		self.y = y

# 建立實體物件，並取得實體屬性資料
p = Point(1,5)
print(p.x + p.y)

#----------------------------Example----------------------------

# FullName 實體物件的設計：分開紀錄姓、名資料的全名
class FullName_1:
	def __init__(self):
		self.first = "Wei Tso"
		self.last = "Chen"

myName_1 = FullName_1()
print("My name is : " , myName_1.first + "," +myName_1.last)
print(f"My name is : {myName_1.first} , {myName_1.last}")

#----------------------------Example----------------------------

class FullName_2:
	def __init__(self , first , last):
		self.first = first
		self.last = last

myName_2 = FullName_2("W.T." , "Chen")
print("My name is : " , myName_2.first + "," +myName_2.last)
print(f"My name is : {myName_2.first} , {myName_2.last}")
name1 = FullName_2("Amber" , "Lan")
print(name1.first , name1.last)
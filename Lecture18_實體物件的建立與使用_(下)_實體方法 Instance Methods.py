'''
---------------------------------------------------------------------
|	此課程程式包含：												 |
|	- Lecture18_實體物件的建立與使用_(下)_實體方法 Instance Methods.py |
|   - Lecture18_1.txt												|
|	- Lecture18_2.txt 												|
---------------------------------------------------------------------
'''


'''
類別的兩種方法
1. 類別與類別屬性
2. 類別與實體物件、實體屬性、實體方法
'''

# 實體屬性
# 封裝在實體物件中的變數

#--------------------------------------------------------

# 實體方法
# 封裝在實體物件中的函式

# 基本語法一
'''
class 類別名稱:
	# 定義初始化函式
	def __init__(self):
		定義實體屬性

	定義實體方法/函式

# 建立實體物件，放入變數 obj 中
obj = 類別名稱()	# 呼叫初始化函式
'''

# 基本語法二
'''
class 類別名稱:
	# 定義初始化函式
	def __init__(self):
		封裝在實體物件中的變數

	def 方法名稱(self , 更多自訂參數):
		方法主體，透過 self 操作實體物件

# 建立實體物件，放入變數 obj 中
obj = 類別名稱()	# 呼叫初始化函式
'''

#--------------------------------------------------------

# 使用實體方法之方式
# 基本語法
'''
實體物件.實體方法名稱(參數資料)
'''

#----------------------------Example----------------------------

class Point:
	def __init__(self , x , y):
		self.x = x
		self.y = y

	def show(self):
		print("x :" , self.x)
		print("y :" , self.y)

	def distance(self , targetX , targetY):
		return ((self.x - targetX)**2 + (self.y - targetY)**2)**0.5

p = Point(3 , 4)	# 建立實體物件
p.show()	# 呼叫實體方法
result = p.distance(0 , 0)	# 計算 座標(3,4) 和 座標(0,0) 之間的距離
print(result)

#--------------------------------------------------------

# File 實體物件的設計：包裝檔案讀取的程式

#----------------------------Example----------------------------

class File:
	def __init__(self , name):	# 建立初始化函式，接受一個檔案名稱
		self.name = name
		self.file = None	# 尚未開啟檔案，所以初期是None

	# 定義開啟檔案的函式 open()
	def open(self):
		# Python 內建開啟檔案的函式 open()
		# 將檔案物件放進 實體屬性file 中
		self.file = open(self.name , mode = "r" , encoding = "utf-8")	# 開啟模式 固定為"r"，encoding 固定為"utf-8"

	# 定義讀取檔案的函式 read()
	def read(self):
		return self.file.read()

# 讀取第一個檔案
file_1 = File("Lecture18_1.txt")
file_1.open()
read_1 = file_1.read()
print(read_1)

# 讀取第二個檔案
file_2 = File("Lecture18_2.txt")
file_2.open()
read_2 = file_2.read()
print(read_2)
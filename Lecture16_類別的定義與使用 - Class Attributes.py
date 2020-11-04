# 類別
# 封裝的變數或函式，統稱：類別的屬性
# 要先定義(建立)類別，然後才能使用類別中封裝的屬性

# 定義類別
'''
class 類別名稱:
	定義封裝的變數
	定義封裝的函式
'''
'''
# 定義 Test 類別
# 其中，x 和 say() 是 Test 類別的屬性
class Test:
	x = 3	# 定義變數
	def say():	# 定義函式
		print("Hello")
'''

#--------------------------------------------------------

# 使用類別
# 基本語法
# 屬性名稱為封裝在類別中的屬性名稱
'''
類別名稱.屬性名稱
'''
'''
Test.x + 3	# 取得屬性 x 的資料為 3
Test.say()	# 呼叫屬性 say 函式
'''

#--------------------------------------------------------

'''
class IO:
	supportedSRCs = ["console" , "file"]
	def read(src):
		print("Read from : " , src)

print(IO.supportedSRCs)
IO.read("file")
'''

class IO:
	supportedSRCs = ["console" , "file"]
	def read(src):
		if src not in IO.supportedSRCs:
			print("Not supported.")
		else:
			print("Read from : " , src)

print(IO.supportedSRCs)
IO.read("file")
IO.read("Internet")
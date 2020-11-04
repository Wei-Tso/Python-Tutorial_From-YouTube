'''
-----------------------------------------
|	此課程程式包含：						|
|	- Lecture13_文字檔案的讀取和儲存.py	|
|   - data.txt							|
|	- data1.txt							|
|	- config.json 						|
-----------------------------------------
'''


# 檔案操作流程
# 開啟檔案 -->> 讀取或寫入 -->> 關閉檔案

# 開啟檔案
# 基本語法
'''
檔案物件 = open(檔案路徑 , mode = 開啟模式)
'''
# 開啟模式
'''
讀取模式 r
寫入模式 w
讀寫模式 r+
'''

#--------------------------------------------------------

# 讀取檔案
# 讀取已經存在的檔案
# 讀取全部文字
'''
檔案物件.read()
'''
# 一次讀取一行
'''
for 變數 in 檔案物件:
	從檔案依序讀取每行文字到變數中
'''
# 讀取 JSON 格式
'''
import json
讀取到的資料 = json.load(檔案物件)
'''

#--------------------------------------------------------

# 寫入檔案
# 寫入文字
'''
檔案物件.write(字串)
'''
# 寫入換行符號
'''
檔案物件.write("這是範例文字\n")
'''
# 寫入 JSON 格式
'''
import json
json.dump(要寫入的資料 , 檔案物件)
'''

#--------------------------------------------------------

# 關閉檔案
# 基本語法
'''
檔案物件.close()
'''

#--------------------------------------------------------

# 最佳實務
'''
# 以下區塊會自動、安全的關閉檔案，不需要再寫 close()
# with 會安全的自動關閉檔案
with open(檔案路徑 , mode = 開啟模式) as 檔案物件:
	讀取或寫入檔案的程式

'''

#--------------------------------------------------------


# 開啟模式	
# encoding  ='utf-8' 可以在輸入中文時，不會出現亂碼
file = open("data.txt" , mode = "w" , encoding  ='utf-8')	
# 操作	
# 新的內容會覆蓋舊的內容	
# 當輸入中文時，會出現亂碼
file.write("Hello File\nSecond Line\n測試中文")	
file.close()	# 關閉
# Ctrl+b 執行後，會產生一個 data.txt 檔案在資料夾中

with open("data.txt" , mode = "w" , encoding = "utf-8") as file:
	file.write("With Version\nHello File\nSecond Line\n測試中文")

with open("data.txt" , mode = "r" , encoding = "utf-8") as file:
	data = file.read()
print(data)



with open("data1.txt" , mode = "w" , encoding = "utf-8") as file:
	file.write("5\n3")

# 把檔案中的數字資料，一行一行的讀取出來，並計算總合
sum = 0
with open("data1.txt" , mode = "r" , encoding = "utf-8") as file:
	for number in file:
		sum = sum + int(number)	# 讀取的數字為"字串型態"，所以要改變型態
print(sum)



import json
with open("config.json" , mode = "r") as file:
	data = json.load(file)
print("Name : " , data["Name"])	# 以字典型態處理
print("Version : " , data["Version"])	# 以字典型態處理
# 修改變數的資料
data["Name"] = "New name"
# 把最新的資料複寫回檔案中
with open("config.json" , mode = "w") as file:
	json.dump(data , file)

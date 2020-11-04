'''
---------------------------------------------
|	此課程程式包含：						 |
|	- Lecture15_網路連線程式、公開資料串接.py |
|   - Company.txt							|
---------------------------------------------
'''


# 網路連線
# import urllib.request

# 下載特定網址資料
'''
import urllib.request as request
with request .urlopen(網址) as response:
	data = response.read()
'''

#--------------------------------------------------------

# 公開資料
'''
JSON、CSV、或其他格式
'''

#--------------------------------------------------------

import urllib.request as request

'''
src = "https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
	data = response.read().decode("utf-8")	# 取得網站的原始碼(HTML、CSS、JS) | 用 decode("utf-8") 處理中文
print(data)
'''
import json
src = "https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=3940ed77-461f-44ef-b3d3-0867f85b94eb"
with request.urlopen(src) as response:
	data = json.load(response)	# 利用 json 模組處理 json 資料格式
# print(data)
# print(type(data))	# dict

dataList = data["result"]["results"]
# print(dataList)
# print(type(dataList))	#list

# for company in dataList:
# 	print(company["公司名稱"])

# 將所有公司名稱另存新檔
with open("Company.txt" , "w" , encoding = "utf-8") as file:
	for company in dataList:
		file.write(company["公司名稱"] + "\n")

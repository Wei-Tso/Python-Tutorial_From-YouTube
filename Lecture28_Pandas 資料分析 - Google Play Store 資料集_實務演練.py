# 資料工程
'''
1. 收集資料
2. 清理資料
3. 分析資料
'''

#----------------------------Example----------------------------

'''
1. 收集資料 : https://bit.ly/2UMcbDI
2. 清理資料
3. 分析資料
'''

import pandas as pd

# 讀取資料
data = pd.read_csv("googleplaystore.csv")

#--------------------------------------------------------

# 觀察資料
print(data)
print(f"資料數量 : {data.shape}")
print(f"資料欄位 : {data.columns}")

#--------------------------------------------------------

# 分析資料 : 評分的各種統計數據
print(data["Rating"])
print(f"平均數 : {data['Rating'].mean()}")
print(f"中位數 : {data['Rating'].median()}")
print(f"前100筆資料的平均 : {data['Rating'].nlargest(100).mean()}")

'''
由於  前100筆資料的平均 = 5.14，大於 5，資料有異常
因此將大於5的資料篩選出來
'''
# condition = data["Rating"] > 5
# filerData = data[condition]
# print(filerData)

'''
確認有資料大於5，因此須將其排除
'''
ratingCondition = data["Rating"] < 5
data = data[ratingCondition]
print(data.shape)

#--------------------------------------------------------

# 分析資料 : 安裝數量的各種統計數據
print(data["Installs"])

'''
由於 data["Installs"] 的資料為 字串型態
因此須對資料做處理
'''
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]" , ""))

installCondition = data["Installs"] > 100000
print(f"安裝數量 > 100000 有幾個 : {data[installCondition].shape[0]}")

#--------------------------------------------------------

# 基於資料的應用 : 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字 : ")
condition = data["App"].str.contains(keyword , case = False)
'''
contains(case = False) : 忽略大小寫
'''

print(data[condition]["App"])
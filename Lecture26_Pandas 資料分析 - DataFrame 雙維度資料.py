# DataFrame
# 雙維度的資料
# 就像是一個表格，有欄和列的概念

#--------------------------------------------------------

# 建立 DataFrame
'''
# 載入 Pandas 模組
import pandas as pd
# 以字典資料為底，建立 DataFrame
pd.DataFrame(字典)
'''

#--------------------------------------------------------

# 資料索引
# 資料的獨立編號，就像試算表中最左邊的編號

# 內建索引
'''
# 載入 Pandas 模組
import pandas as pd
# 以字典資料為底，建立 DataFrame
pd.DataFrame(字典)
'''

# 自訂索引
'''
# 載入 Pandas 模組
import pandas as pd
# 以字典資料為底，建立 DataFrame
pd.DataFrame(字典 , index = 索引列表)
'''

#--------------------------------------------------------

# 觀察資料

# 資料數量
'''
import pandas as pd
data=pd.DataFrame(字典)
# 印出 size 屬性
print(data.size)
'''

# 資料形狀
'''
import pandas as pd
data=pd.DataFrame(字典)
# 印出 shape 屬性
print(data.shape)
'''

# 資料索引
'''
import pandas as pd
data=pd.DataFrame(字典 , index=索引列表)
# 印出 index 屬性
print(data.index)
'''

#--------------------------------------------------------

# 取得資料

# 取得 「列」(row) 資料
# 整列的資料：列(row) 在試算表中橫向的資料

# 根據順序取一整列
'''
import pandas as pd
data=pd.DataFrame(字典)
# 取得一整列 data.iloc[順序]
print(data.iloc[1])	# Series 型態
'''

# 根據索引取一整列
'''
import pandas as pd
data=pd.DataFrame(字典 , index=索引列表)
# 取得一整列 data.loc[索引]
print(data.loc[索引])	# Series 型態
'''

#--------------------------------------------------------

# 取得資料

# 取得 「欄」(column) 資料
# 整列的資料：欄(column) 在試算表中直向的資料

# 根據名稱取一整欄
'''
import pandas as pd
data=pd.DataFrame(字典)
# 取得一整欄 data[欄位名稱]
print(data[欄位名稱])	# Series 型態
'''

#--------------------------------------------------------

# 建立新的欄位
'''
import pandas as pd
data=pd.DataFrame(字典)
# 以下語法建立新的欄位
data["新欄位名稱"] = 列表資料
data["新欄位名稱"] = Series 型態資料
'''

#----------------------------Example----------------------------

import pandas as pd
'''
data = pd.DataFrame({
	"name":["Amy" , "Bob" , "Charles"],
	"salary":[30000 , 50000 , 40000]
})
'''
data = pd.DataFrame({
	"name":["Amy" , "Bob" , "Charles"],
	"salary":[30000 , 50000 , 40000]
} , index = ["a" , "b" , "c"])

print(data)

print(f"資料數量 : {data.size}")
print(f"資料形狀 : (列 , 欄) = {data.shape}")
print(f"資料索引 : {data.index}")

print(f"取得第二列: \n{data.iloc[1]}")
print(f"取得第c列 : \n{data.loc['c']}")

print(f"取得 name 欄位 : \n{data['name']}")

names = data["name"]	# 取得單維度的 Series 資料
print(f"把 name 全部轉大寫 : \n{names.str.upper()}")
salaries = data["salary"]
print(f"薪水的平均值 : \n{salaries.mean()}")

data["revenue"] = [500000 , 400000 , 300000]
data["rank"] = pd.Series([3 , 6 , 1] , index = ["a" , "b" , "c"])
# 因為 DataFrame 有 index，所以 Series 要有相對應的 index
data["CP"] = data["revenue"] / data["salary"]
print(data)
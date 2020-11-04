# Series
# 單維度的資料
# 就像是一個列表、或是試算表中直向的欄位資料

#--------------------------------------------------------

# 建立 Series
'''
# 載入 Pandas 模組
import pandas as pd
# 以列表資料為底，建立 Series
pd.Series(資料列表)
'''

#--------------------------------------------------------

# 資料索引
# 資料的獨立編號，就像試算表中最左邊的編號

# 內建索引
'''
# 載入 Pandas 模組
import pandas as pd
# 以列表資料為底，建立 Series
pd.Series(資料列表)
'''

# 自訂索引
'''
# 載入 Pandas 模組
import pandas as pd
# 以列表資料為底，建立 Series
pd.Series(資料列表 , index = 索引列表)
'''

#--------------------------------------------------------

# 觀察資料

# 資料型態
'''
import pandas as pd
data=pd.Series(資料列表)
# 印出 dtype 屬性
print(data.dtype)
'''

# 資料數量
'''
import pandas as pd
data=pd.Series(資料列表)
# 印出 size 屬性
print(data.size)
'''

# 資料索引
'''
import pandas as pd
data=pd.Series(資料列表 , index=索引列表)
# 印出 index 屬性
print(data.index)
'''

#--------------------------------------------------------

# 取得資料

# 根據順序取值
'''
import pandas as pd
data=pd.Series(資料列表)
# 取得資料 data[順序]
print(data[1])
'''

# 根據索引取值
'''
import pandas as pd
data=pd.Series(資料列表 , index=索引列表)
# 取得資料 data[索引]
print(data[索引])
'''

#--------------------------------------------------------

# 數字運算

# 數學、統計相關
'''
import pandas as pd
data=pd.Series([3,10,20,5,-12])
# 各種 數學、統計 運算
print(data.sum() , data.max() , data.prod())		# 加法總和、最大值、乘法總和
print(data.mean() , data.median() , data.std())		# 平均數、中位數、標準差
print(data.nlargest(3) , data.nsmallest(2))			# 取前三大的數字、取最小的兩個數字
'''

#--------------------------------------------------------

# 字串運算
'''
import pandas as pd
data=pd.Series(["你好" , "Python" , "Pandas"])
# 各種字串操作，都定義在 str 底下
print(data.str.lower() , data.str.upper() , data.str.len())		# 將所有字串變小寫、將所有字串變大寫、自串長度
print(data.str.cat(sep=",") , data.str.contains("P"))			# 將所有字串以","串再一起、判斷每一字串是否包含"P"
print(data.str.replace("你好" , "Hello"))						# 將字串做取代："你好" 取代為 "Hello"
'''

#----------------------------Example----------------------------

import pandas as pd

# data = pd.Series([5,4,-2,3,7])
# print(data)

dataNumber = pd.Series([5,4,-2,3,7] , index = ["a" , "b" , "c" , "d" , "e"])

print(dataNumber)

print(f"資料型態 : {dataNumber.dtype}")
print(f"資料數量 : {dataNumber.size}")
print(f"資料索引 : {dataNumber.index}")

print(dataNumber[2] , dataNumber[0])
print(dataNumber["e"] , dataNumber["d"])

print(f"最大值 : {dataNumber.max()}")
print(f"總和 : {dataNumber.sum()}")
print(f"標準差 : {dataNumber.std()}")
print(f"中位數 : {dataNumber.median()}")
print(f"最大的三個數 : \n{dataNumber.nlargest(3)}")


dataString=pd.Series(["你好" , "Python" , "Pandas"])
print(dataString.str.lower())
print(dataString.str.len())
print(dataString.str.cat(sep = "-"))
print(dataString.str.contains("P"))
print(dataString.str.replace("你好" , "Hello"))
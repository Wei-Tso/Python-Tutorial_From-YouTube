# Pandas
'''
概念類似試算表的資料分析套件
'''

#--------------------------------------------------------

# 安裝套件
# PIP 套件管理工具：安裝 Python 時，就一起安裝在電腦裡了
'''
# 安裝 Pandas
pip install pandas
'''

#--------------------------------------------------------

# Series
# 單維度的資料
# 就像是一個列表、或是試算表中直向的欄位資料

#--------------------------------------------------------

# 建立 Series
'''
# 載入 Pandas 模組
import pandas as pd
# 以列表資料為底，建立 Series
pd.Series(列表)
'''

#--------------------------------------------------------

# 使用 Series
'''
import pandas as pd
data = pd.Series(列表)
data.max()	# 找到最大值
data.median()	# 計算中位數
data = data*2	# 放大2倍
'''

#--------------------------------------------------------

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

# 取得特定欄(直向)
'''
import pandas as pd
data = pd.DataFrame(字典)
data["欄位名稱"]
'''

#--------------------------------------------------------

# 取得特定列(橫向)
'''
import pandas as pd
data = pd.DataFrame(字典)
data.iloc[列編號]	# 列編號由0開始
'''

#----------------------------Example----------------------------

import pandas as pd
dataSeries = pd.Series([20 , 10 , 15])
print(dataSeries)
print(dataSeries.max())
print(dataSeries.median())
data = dataSeries*2
print(data)

dataCompare = data==20
print(dataCompare)

dataDataFrame = pd.DataFrame({"name":["Amy" , "John" , "Bob"] , "salary":[30000 , 50000 , 40000]})
print(dataDataFrame)
print(dataDataFrame["name"])
print(dataDataFrame.iloc[0])
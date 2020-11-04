# Series

'''
# 建立 Series 資料
import pandas as pd
data = pd.Series(列表)
# 建立篩選條件(與資料數量對應的布林值)
condition = [True , False , True]
# 根據條件完成篩選
filteredData = data[condition]
'''

'''
# 建立 Series 資料
import pandas as pd
data = pd.Series(列表)
# 建立篩選條件(直接透過比較運算產生)
condition = data > 5
# 根據條件完成篩選
filteredData = data[condition]
'''

#--------------------------------------------------------

# DataFrame

'''
# 建立 DataFrame 資料
import pandas as pd
data = pd.DataFrame(字典)
# 建立篩選條件(與資料數量對應的布林值)
condition = [True , False , True]
# 根據條件完成篩選
filteredData = data[condition]
'''

'''
# 建立 DataFrame 資料
import pandas as pd
data = pd.DataFrame(字典)
# 建立篩選條件(直接透過比較運算產生)
condition = data[欄位名稱] > 5
# 根據條件完成篩選
filteredData = data[condition]
'''

#----------------------------Example----------------------------

import pandas as pd

dataSeries = pd.Series([30 , 15 , 20])
condition = [True , False , True]
filteredSeriesData = dataSeries[condition]
print(filteredSeriesData)

condition_1 = dataSeries > 18
print(condition_1)

dataSeries_2 = pd.Series(["你好" , "Python" , "Pandas"])
condition_2 = [False , True , True]
filteredSeriesData_2 = dataSeries_2[condition_2]
print(filteredSeriesData_2)

condition_2_1 = dataSeries_2.str.contains("P")
print(condition_2_1)

dataFrame = pd.DataFrame({
	"name":["Amy" , "Bob" , "Charles"],
	"salary":[30000 , 50000 , 40000]
})
conditionData = [False , True , True]
filteredDataFrame = dataFrame[conditionData]
print(filteredDataFrame)

conditionData_1 = dataFrame["salary"] >= 40000
print(conditionData_1)

conditionData_2 = dataFrame["name"] == "Amy"
print(conditionData_2)
print(dataFrame[conditionData_2])
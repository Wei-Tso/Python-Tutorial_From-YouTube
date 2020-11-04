# 亂數模組
import random


# 從列表中隨機選取一個資料
random.choice([0,1,5,8])
# 從列表中隨機選取2個資料，但是不能超過列表的長度
random.sample([0,1,5,8] , 2)	


# 將列表的資料 「就地」 隨機調換順序
data = [0,1,5,8]
random.shuffle(data)
print(data)


#--------------------------------------------------------

# 隨機亂數

# 取得 0.0 ~ 1.0 之間的隨機亂數，且每一個數出現的機率相同
# 基本語法一
random.random()
# 基本語法二，.uniform() 表示機率相同
random.uniform(0.0 , 1.0)
random.uniform(1 , 5)	# 1 ~ 5 之間的隨機亂數


#--------------------------------------------------------

# 常態分配亂數

# 取得 平均數100 、標準差10 的常態分配亂數
random.normalvariate(100 , 10)


#--------------------------------------------------------

# 統計模組
import statistics

# 計算列表中數字的平均數
statistics.mean([1,4,6,9])
# 計算列表中的中位數
statistics.median([1,4,6,9])
# 計算列表中的標準差：代表資料的散佈狀況
statistics.stdev([1,4,6,9])


#--------------------------------------------------------

import random
dataChoice = random.choice([1,3,6,10,30,-45,-27,99])
print("dataChoice : " , dataChoice)
print("-------------------------------------------------")

dataSample = random.sample([1,3,6,10,30,-45,-27,99] , 4)
print("dataSample : " , dataSample)
print("-------------------------------------------------")

dataShuffle = [1,3,6,10,30,-45,-27,99]
print(dataShuffle)
random.shuffle(dataShuffle)
print("dataShuffle : " , dataShuffle)
print("-------------------------------------------------")

dataRandom = random.random()
print("dataRandom : " , dataRandom)
print("-------------------------------------------------")

dataUniform = random.uniform(60 , 100)
print("dataUniform : " , dataUniform)
print("-------------------------------------------------")

# 平均數100、標準差10，資料多數在 90 ~ 110 之間
dataNormal = random.normalvariate(100 , 10)
print("dataNormal : " , dataNormal)
print("-------------------------------------------------")

# 平均數0、標準差5，資料多數在 -5 ~ 5 之間
dataNormal2 = random.normalvariate(0 , 5)
print("dataNormal2 : " , dataNormal2)
print("-------------------------------------------------")

#--------------------------------------------------------

import statistics as stat
dataMean = stat.mean([1,4,5,8])
print("dataMean : " , dataMean)
print("-------------------------------------------------")

dataMedian = stat.median([1,2,3,4,5,8,100])
print("dataMedian : " , dataMedian)
print("-------------------------------------------------")

dataSTdev = stat.stdev([1,2,3,4,5,8,100])
print("dataSTdev : " , dataSTdev)

# 有序可變動列表 List []

# 建立新的列表grades

grades = [12, 60, 15, 70, 90]
print(grades)
# 可以使用索引查詢列表的資料
print(grades[0])
print(grades[1])
print(grades[2])
print(grades[3])
print(grades[4])
# 可以更新列表的資料
grades[0] = 55
print(grades[0])
# 取得列表中的一些元素
print(grades[1:4])	# 取得索引值為1, 2, 3的元素
# 連續刪除列表中從索引值0~索引值4(不包括)的資料
grades[1:4] = []
print(grades)

grades = [12, 60, 15, 70, 90]
# 列表串接
grades = grades + [12, 33]
print(grades)
# 取得列表的長度 len(列表)
print(len(grades))

# 巢狀列表
data = [[3, 4,  5] , [6, 7, 8]]
print(data)
print(data[0])
print(data[1])
print("---------------------------")
print(data[0][0])
print(data[0][1])
print(data[0][2])
print("---------------------------")
print(data[1][0])
print(data[1][1])
print(data[1][2])
print("---------------------------")
print(data[0][0:2])
print("---------------------------")
data[0][0:2] = [10, 11, 12, 13]
print(data)
print(data[0])


#--------------------------------------------------------

# 有序不可變動列表 Tuple ()
data = (3, 4, 5)
print(data)
print(data[0])
print(data[1])
print(data[2])
print("---------------------------")
print(data[0:2])
print("---------------------------")
# data[0] = 5	# 錯誤：Tuple 的資料不可變動
data = data + (12, 33)
print(data)
# 集合 Set{}
# 一群資料，沒有順序性

# 判斷資料是否存在 -->> 使用 in 或是 not in
s1 = {3, 4, 5}
print(3 in s1)
print(10 in s1)
print(10 not in s1)

# 交集 &：取兩個集合中，相同的資料
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 & s2
print(s3)

# 聯集 |：取兩個集合中的所有資料，但不重複
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 | s2
print(s3)

# 差集 -：從 s1 中，減去和 s2 重疊的部分
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 - s2
print(s3)
s4 = s2 - s1
print(s4)

# 反交集 ^：取兩個集合中，不重疊的部分
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1 ^ s2
print(s3)

# set(字串)：將字串中的文字拆解成集合
s = set("Hello")
print(s)
print("H" in s)


#--------------------------------------------------------

# 字典 Dictionary{"key" : "value"}，key-value的配對

dic = {"apple":"蘋果" , "bug":"蟲"}
print(dic)
print(dic["apple"])	# 利用 key 取得 value
dic["apple"] = "小蘋果"	# 修改 value
print(dic["apple"])

# 判斷 key 是否存在 -->> 使用 in 或是 not in
dic = {"apple":"蘋果" , "bug":"蟲"}
print("apple" in dic)
print("test" in dic)
print("test" not in dic)

# 刪除鍵值對 -->> 使用 del
# 以 key 當代表，但刪除時會將整個 key-value對 刪除
dic = {"apple":"蘋果" , "bug":"蟲"}
del dic["apple"]
print(dic)

# 以列表資料為基礎建立字典
# dic = {"key":"value" for x in 列表}
# dic = {x:x*2 for x in [3, 4, 5]}
dic = {x:x*2 for x in [3, 4, 5]}
print(dic)

data = [1, 2, 3, 4, 5]
dic1 = {x:x**3 for x in data}
print(dic1)

# 數字運算
x1 = 3 + 6 # 加
print(x1)
x2 = 3 - 6 # 減
print(x2)
x3 = 3 * 6 # 乘
print(x3)
x4 = 3 / 6 # 除_小數除法
print(x4)
x5 = 3 // 6 # 除_整數除法
print(x5)
x6 = 2 ** 3 # 2的3次方
print(x6)
x7 = 7 % 3 # 取餘數
print(x7)


# 字串運算

s = 'hello'
print(s)
s1 = "Hell\"o\""	# 雙引號中有雙引號，可用 \ -->> 跳脫
print(s1)
s2 = "Hello" + "world"	# 自串用 '+' 進行串接
print(s2)
s3 = "Hello" " world"	# 自串也可用 ' ' 進行串接
print(s3)
s4 = "Hello\nworld"	# \n 表示換行
print(s4)
s5 = """Hello

world"""	# 用3個引號可直接換行
print(s5)
s6 = "hello" * 3	# 將字串重複
print(s6)
s7 = "Hello" * 3 + "world"
print(s7)


# 字串會對內部字元編號(索引)，從0開始算起
s = "Hello"
print(s[2])
print(s[1:4])	# 包含開頭，不包含結尾
print(s[1:])	# 從開頭算起，取得後面所有的字元
print(s[:4])
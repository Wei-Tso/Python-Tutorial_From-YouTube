# while 基本語法
'''
while 布林值:
	若布林值為True，執行命令
	回到上方，做下一次的迴圈判斷
'''

n = 1
while n < 5:
	print("資料為:", n)
	n += 1

'''
無窮迴圈
n = 1
while True:
	print(n)
	n += 1
'''

# 1+2+...+10
n = 1
sum = 0	# 紀錄累加的結果
while n <= 10:
	sum = sum + n
	n += 1
print(sum)


#--------------------------------------------------------

# for 基本語法
'''
for 變數名稱 in 列表或字串:
	將列表中的項目或字串中的字元逐一取出，逐一處理
'''

for x in [4, 1, 2]:
	print(x)

for c in "Hello":
	print(c)

# for 經常使用 range()：可以製造出連續數字的列表
'''
for 變數名稱 in range(3):
相當於
for 變數名稱 in [0, 1, 2]:
'''
'''
for 變數名稱 in range(3, 6):
相當於
for 變數名稱 in [3, 4, 5]:
'''

for x in range(5):
	print(x)

for x in range(5, 10):
	print(x)

# 1+2+...+10
sum = 0
for x in range(11):
	print(x)
	sum = sum + x
print(sum)

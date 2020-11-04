# break	強制結束迴圈
# break 一定使用在迴圈裡面
# 基本語法一
'''
while 布林值:
	break
'''
# 基本語法二
'''
for 變數名稱 in 列表或字串:
	break
'''

n = 0
while n < 5:
	if n == 3:
		break
	print(n)	# 印出迴圈中的 n
	n += 1
print("最後的 n: ", n)	# 印出迴圈結束後的 n


#--------------------------------------------------------

# continue 強制繼續下一圈
# continue 一定使用在迴圈裡面
# 基本語法一
'''
while 布林值:
	continue
'''
# 基本語法二
'''
for 變數名稱 in 列表或字串:
	continue
'''

# 當 x=0 ，因為 x%2==0 為 True ，所以執行 continue ，不會執行 n+=1 ，往下一圈 x=1 繼續執行判斷
# 當 x=2 ，因為 x%2==0 為 True ，所以執行 continue ，不會執行 n+=1 ，往下一圈 x=3 繼續執行判斷
n = 0
for x in [0, 1, 2, 3]:
	if x % 2 == 0:
		print(f"當x為: {x} 時，執行 continue")
		continue
	n += 1
	print(f"此時x為: {x}")
print(n)


#--------------------------------------------------------

# else	
# 基本語法一
'''
while 布林值:
	若布林值為True，執行命令
	回到上方，做下一次迴圈判斷
else:
	迴圈結束前，執行此區塊命令
'''
# 基本語法二
'''
for 變數名稱 in 列表或字串:
	將列表中的項目或字串中的字元逐一取出 ，逐一處理
else:
	迴圈結束前，執行此區塊命令
'''

n = 1
while n < 5:
	print(f"此時n為: {n}")
	n += 1
else:
	print(f"迴圈結束時的n為: {n}")


for c in "Hello":
	print(f"此時c為: {c}")
else:
	print(f"迴圈結束時的c為: {c}")

sum = 0
for x in range(11):
	sum = sum + x
else:
	print(sum)	# 印出 1+2+...+10 的結果
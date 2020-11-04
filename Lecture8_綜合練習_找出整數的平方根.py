# 找出整數的平方根
# 輸入 9 , 得到 3
# 輸入 11 , 得到 [沒有]整數的平方根
n = input("輸入一個正整數 : ")
n = int(n)
for i in range(n):
	if i**2 == n:
		print(f"{n} 的平方根為 : {i}")
		break	# 用 break 強制結束迴圈時，不會執行 else 區塊
else:
	print(f"{n} 沒有整數平方根")
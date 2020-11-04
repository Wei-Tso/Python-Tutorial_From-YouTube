# 基本語法一
'''
if 布林值:
	若布林值為True，執行命令
'''
# 基本語法二
'''
if 布林值:
	若布林值為True，執行命令
else:
	若布林值為False，執行命令
'''
# 基本語法三
'''
if 布林值一:
	若布林值一為True，執行命令
elif 布林值二:
	若布林值二為True，執行命令
else:
	若布林值一和二都False，執行命令
'''

x = input("請輸入數字:")	# 輸入的數字為字串型態
x = int(x)	# 將字串型態轉換成數字型態

if x > 100:
	print("大於100")
else:
	print("小於等於100")

if x > 200:
	print("大於200")
elif x > 100:
	print("大於100，小於等於200")
else:
	print("小於等於100")


# 四則運算
n1 = int(input("請輸入數字一:"))
n2 = int(input("請輸入數字二:"))
print(n1+n2)
op = input("請輸入運算 +, -, *, / : ")
if op == "+":
	print(n1+n2)
elif op == "-":
	print(n1-n2)
elif op == "*":
	print(n1*n2)
elif op == "/":
	print(n1/n2)
else:
	print("不支援的運算")
#--------------------------------------------------------

# switch
# 截至 Python3.6，不支援 switch 語法
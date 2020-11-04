'''
-----------------------------
|	此課程程式包含：		 |
|	- modules				|
|		- geometry.py		|
-----------------------------
'''


# Module
# 獨立的程式檔案
# 將程式寫在一個檔案中，此檔案可重複載入使用
# 先載入模組，在使用模組中的函式或變數

# 載入模組
# 基本語法一
'''
import 模組名稱
'''
# 基本語法二
'''
import 模組名稱 as 模組別名
'''

#--------------------------------------------------------

# 使用模組
# 基本語法
'''
模組名稱或別名.函式名稱(參數資料)
模組名稱或別名.變數資料
'''

#--------------------------------------------------------

# 內建模組
# Python 有許多的內建模組
'''
sys : 取得系統相關資訊
'''

import sys
print(sys.platform)	# 印出作業系統
print(sys.maxsize)	# 印出整數型態的最大值
print(sys.path)		# 印出搜尋模組的路徑

import sys as s
print(s.platform)	# 印出作業系統
print(s.maxsize)	# 印出整數型態的最大值
print(s.path)		# 印出搜尋模組的路徑


#--------------------------------------------------------

# 自訂模組

# 建立幾何運算模組
# 建立檔案 geometry.py，定義平面幾何運算用的函式

# 載入與使用
# 載入 geometry 模組，並使用模組中定義的功能

# 將 geometry.py 與 Lecture11.py 放在同一資料夾中
'''
import geometry
result1 = geometry.distance(1, 1, 5, 5)
print(result1)
result2 = geometry.slope(1, 1, 5, 5)
print(result2)
'''

# 將 geometry.py 放在 modules 資料夾中
# 需調整搜尋模組的路徑
import sys
print(sys.path)
sys.path.append("modules") # 在模組的搜尋路徑列表中 [新增路徑]
print(sys.path)

import geometry
result1 = geometry.distance(1, 1, 5, 5)
print(result1)

result2 = geometry.slope(1, 1, 5, 5)
print(result2)

result3 = geometry.add(-1,2,3,-4)
print(result3)

result4 = geometry.subtract(-1,2,3,-4)
print(result4)

result5 = geometry.multiply(-1,2,3,-4)
print(result5)

result6 = geometry.divide(-1,2,-4,-8,100)
print(result6)

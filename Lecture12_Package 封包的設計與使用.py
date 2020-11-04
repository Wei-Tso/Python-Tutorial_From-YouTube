'''
-----------------------------
|	此課程程式包含：		 |
|	- main.py				|
|	- geometry			    |
|		- __init__.py	    |
|		- point.py		    |
|		- line.py		    |
-----------------------------
'''


# 封包
# 包含模組的資料夾，用來整理、分類模組程式
# 資料夾 <--> 封包	|	檔案 <--> 模組

# 建立封包
# 專案檔案配置
# 有 __init__.py 檔案的資料夾才會被當作是封包
# 一定要有 __init__.py 這個檔案，但是 __init__.py 程式內容可以空白
'''
- 專案資料夾
	- 主程式.py
	- 封包資料夾
		- __init__.py
		- 模組一.py
		- 模組二.py
'''
'''
- 專案資料夾
	- main.py
	- geometry
		- __init__.py
		- point.py
		- line.py
'''

#--------------------------------------------------------

# 使用封包
# 基本語法一
'''
import 封包名稱.模組名稱
'''
# 基本語法二
'''
import 封包名稱.模組名稱 as 模組別名
'''
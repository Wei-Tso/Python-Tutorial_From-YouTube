# 基本流程
'''
1. 連線到特定網址，抓取資料
2. 解析資料，取得實際想要的部分
'''

#--------------------------------------------------------

# 抓取資料
# 盡可能地讓程式模仿一個普通使用者的樣子，因為網站都不希望人家用程式去抓取資料

#--------------------------------------------------------

# 解析資料
'''
JSON 格式資料
使用內建的 json 模組即可
'''

# 大多數時候取得的資料為 HTML 格式資料
'''
HTML 格式資料
使用第三方套件 BeautifulSoup 來做解析
'''

#--------------------------------------------------------

# 安裝套件
# PIP 套件管理工具：安裝 Python 時，就一起安裝在電腦裡了
'''
# 安裝 BeautifulSoup
pip install beautifulsoup4
'''

#----------------------------Example----------------------------

# 抓取 PTT 電影版 的網頁原始碼(HTML)
import urllib.request as req
# 改善前
'''
url = "https://www.ptt.cc/bbs/movie/index.html"
with req.urlopen(url) as response:
	data = response.read().decode("utf-8")
print(data)
'''
'''
執行後，跳出錯誤訊息：urllib.error.HTTPError: HTTP Error 403: Forbidden
連線被拒絕，因為我們的程式看起來就不像是一個正常的，不像一個正常的使用者去做連線
'''
'''
如何改善，請參考影片內容
'''

# 改善後
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url , headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"})
with req.urlopen(request) as response:
	data = response.read().decode("utf-8")
#print(data)

# 解析原始碼，取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data , "html.parser")	# 讓 BeautifulSoup 協助解析 HTML 格式文件
print(root.title.string)	# 先抓到 標籤title，再抓標籤裡的文字 string
titles = root.find("div" , class_ = "title")	# 尋找 class="title" 的 div 標籤
print(titles)
print(titles.a.string)	# 先抓到 標籤div class="title"，再抓裡面的 標籤a，再抓 標籤a 裡的文字 string
'''
執行後，只找到其中一個：find() 會找到其中一個符合的標籤
'''
print("-----------------------------------------------")
'''
尋找 所有 class="title" 的 div 標籤：find_all()
'''
titles_all = root.find_all("div" , class_ = "title")	# 尋找 class="title" 的 div 標籤
print(titles_all)	# 以 列表 儲存所有資料
for all_title in titles_all:
	if all_title.a != None:	# 如果標題含有 標籤a，代表沒有被刪除，印出來
		print(all_title.a.string)
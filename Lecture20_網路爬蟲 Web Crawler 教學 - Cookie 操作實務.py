# 基本流程
'''
1. 連線到特定網址，抓取資料
2. 解析資料，取得實際想要的部分
'''

#--------------------------------------------------------

# Cookie
'''
網站存放在瀏覽器的一小段內容
'''

#--------------------------------------------------------

# 與伺服器的互動
'''
如果使用者的瀏覽器中有放一個Cookie，在連線時，Cookie 被放在 Request Headers 中送出
'''

#--------------------------------------------------------

# 追蹤連結
# 連續抓取頁面實務：解析頁面的超連結，並結合程式邏輯完成

#----------------------------Example----------------------------

# 抓取 PTT 八卦版 的網頁原始碼(HTML)
import urllib.request as req

def getData(url):

	# 建立一個 Request 物件，附加 Request Headers 的資訊
	request = req.Request(url , headers={
		"cookie":"over18=1",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
	})
	'''
	八卦版與電影版不同
	八卦板會有 "是否滿18歲" 的選項，會呈現出 "cookie":"over18=1" 中
	因此，若 headers{} 沒有加上 "cookie":"over18=1"，會是確認畫面的原始碼，而不是看板文章列表的原始碼
	'''

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

	# 抓取上一頁的連結
	nextLink = root.find("a" , string = "‹ 上頁")	# 找到內文是 ‹ 上頁 的 a 標籤
	return nextLink["href"]	# a 標籤中的 href 屬性

# 抓取一個頁面的標題
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
	pageURL = "https://www.ptt.cc" + getData(url)
	count+=1
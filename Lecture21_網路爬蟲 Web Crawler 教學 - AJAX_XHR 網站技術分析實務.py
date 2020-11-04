# 基本流程
'''
1. 連線到特定網址，抓取資料
2. 解析資料，取得實際想要的部分
'''

#--------------------------------------------------------

# AJAX
'''
網頁前端的 JavaScript 程式技術(又名為 XHR)
'''

#--------------------------------------------------------

import urllib.request as req
# 抓取 Medium.com 的文章資料
url = "https://medium.com/_/api/home-feed"

# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url , headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
	})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8") # 根據觀察，取得的資料是 JSON 格式

# 解析 JSON 格式的資料，取得每篇文章的標題，因此不使用 BeautifulSoup
import json
data = data.replace("])}while(1);</x>" , "")
data = json.loads(data) # 把原始的 JSON 資料解析成字典/列表的表示形式
# print(data)

# 取得 JSON 資料中的文章標題
posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key]
    print(post["title"])
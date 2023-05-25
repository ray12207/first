import requests                      # 所有爬蟲第一行一定寫這個，要用 requests 去抓資料
from bs4 import BeautifulSoup

res = requests.get("https://www.104.com.tw/jobs/search/?keyword=%E5%A4%A7%E6%95%B8%E6%93%9A&order=1&jobsource=2018indexpoc&ro=0")
soup = BeautifulSoup(res.text)       # 把 res.text 丟進去煮湯~~~

# print(res)                         # 回傳 200 代表 request成功了~~~
# print(res.text)                    # 成功後把文本 print 出來瞧瞧~~~

print(soup)

# 所有網頁爬蟲基本上前面五行都是醬子~~~
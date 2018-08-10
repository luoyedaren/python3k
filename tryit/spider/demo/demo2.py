# -*- coding: utf-8 -*-
import requests
import re

# header 不加  部分网站会禁止抓取
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


r = requests.get("https://www.zhihu.com/explore", headers=headers)
# r = requests.get("https://www.zhihu.com/explore")
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(type(titles))
print(titles)
for s in titles:
    if type(s) == str:
        print(s)
    else:
        print(s)



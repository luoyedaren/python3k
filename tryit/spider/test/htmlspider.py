# -*- coding: utf-8 -*-

# doc http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
import requests,re
from bs4 import BeautifulSoup
import json
import logging,traceback
import os

# pattern = re.compile('rc.*?hr>(.*?)</p>',re.S)
# findStr = re.findall(pattern,req.text)
# print(findStr)

codeType = 'gb2312'

def getPoem(url,data = {'kid':'001'},codeType=codeType):
    d = {}
    req = requests.get(url,data)
    # 编码转换 工具自动转换编码失败情况时使用
    req.encoding=codeType
    # 使用soup
    soup = BeautifulSoup(req.text,'lxml')
    d['title']= soup.h1.string
    # print(soup.h1.string)
    poem = list(soup.find_all(class_='memo')[0])
    author = soup.find(class_='author').string
    # print(author)
    d['chaodai']=author.split('・')[0]
    d['author']=author.split('・')[1]
    try:
        list1 = []
        for p in poem:
            if not isinstance(p,str):
                pass
            else:
                np = p.strip()
                list1.append(np)
        d['poem']=list1
    except Exception as e:
        logging.exception(e)

    # print(d)
    return d


def save_poem(path,target):
    try:
        with open(path,'w',encoding='GB18030') as f:
            f.write(target)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    s = ''
    for i in range(10):
        url = 'http://www.guoxue.com/365/index.php'
        if i == 0:
            continue
        print('============== %s ================' % i)
        data = {'kid': '00'+str(i)}
        target = getPoem(url,data)
        print(json.dumps(target,ensure_ascii=False))
        s += json.dumps(target, ensure_ascii=False)
    path = 'poem.txt'
    save_poem(path,s)



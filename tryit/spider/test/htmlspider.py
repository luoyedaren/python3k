# -*- coding: utf-8 -*-

# doc http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
import requests, re
from bs4 import BeautifulSoup
import json
import logging, traceback
import csv, time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S', filename='myapp.log', filemode='a')

# pattern = re.compile('rc.*?hr>(.*?)</p>',re.S)
# findStr = re.findall(pattern,req.text)
# logging(findStr)

codeType = 'gb2312'


def getPoem(url, data={'kid': '001'}, codeType=codeType):
    d = {}
    req = requests.get(url, data)
    # 编码转换 工具自动转换编码失败情况时使用
    req.encoding = codeType
    # 使用soup 按节点查找元素
    soup = BeautifulSoup(req.text, 'lxml')
    d['title'] = soup.h1.string
    # logging.(soup.h1.string)
    # find_all 查找所有class_ 是 memo的元素
    poem = list(soup.find_all(class_='memo')[0])
    author = soup.find(class_='author').string
    # logging.(author)
    d['chaodai'] = author.split('・')[0]
    d['author'] = author.split('・')[1]
    try:
        list1 = []
        for p in poem:
            if not isinstance(p, str):
                pass
            else:
                np = p.strip()
                list1.append(np)
        d['poem'] = ''.join(list1)
    except Exception as e:
        logging.exception(e)

    # logging.(d)
    return d


def save_poem_json(path, target):
    try:
        with open(path, 'w', encoding='GB18030') as f:
            f.write(target)
    except Exception as e:
        logging.exception(e)


def save_poem_with_csv(path, target):
    with open(path, 'w', encoding='GB18030') as f:
        field = ['id', 'title', 'chaodai', 'author', 'poem']
        writer = csv.DictWriter(f, fieldnames=field)
        # writer.writerow(['标题','朝代','作者','诗词'])
        writer.writeheader()
        for ss in target:
            writer.writerow(ss)


if __name__ == '__main__':
    s = ''
    listdict = []
    for i in range(10):
        url = 'http://www.guoxue.com/365/index.php'
        if i == 0:
            continue
        logging.info('============== %s ================' % i)
        data = {'kid': '00' + str(i)}
        target = getPoem(url, data)
        target['id'] = i
        # logging.info(json.dumps(target, ensure_ascii=False))
        s += json.dumps(target, indent=2, ensure_ascii=False)
        listdict.append(target)
    path = 'poem-' + time.strftime('%Y-%m-%d') + '.json'
    save_poem_json(path, s)
    path1 = 'poem-' + time.strftime('%Y-%m-%d') + '.csv'
    save_poem_with_csv(path=path1, target=listdict)

import json
import time
from requests import Response
import scrapy
from bilibili.items import CommentItem
import sys
sys.path.append("...")
from main import url
import requests
from lxml import etree


r = requests.get(url)
html = etree.HTML(r.text)
title = html.xpath('//*[@id="viewbox_report"]/h1/text()')[0]
print('Title:', title)


def bv2av(x):
    import re
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608
    def b2a(x):
        r = 0
        for i in range(6):
            r += tr[x[s[i]]] * 58 ** i
        return (r - add) ^ xor
    if 'BV' in x:
        p = r'(BV[a-zA-Z0-9]{10})'
        bvid = re.findall(p, x)[0]  
        id = b2a(bvid)
    return id


class CommentSpider(scrapy.Spider):
    name = "comment"
    allowed_domains = ["bilibili.com"]
    offset = 1
    old_url = url
    aid = bv2av(old_url)
    url = 'https://api.bilibili.com/x/v2/reply/main?csrf=f82f3a501a426bc37af66fa0e68f3391&mode=3&next={}&oid={}&plat=1&seek_rpid=&type=1'
    start_urls = [url.format(str(offset),str(aid))]

    def start_requests(self):
        yield scrapy.Request(url = self.start_urls[0], callback = self.parse, dont_filter = True)
    
    def parse(self, response):
        comment_items = json.loads(response.body.decode('UTF-8'))['data']['replies']
        if comment_items != []:
            for item in comment_items:
                comment = CommentItem()
                comment['name'] = item['member']['uname']
                comment['uid'] = item['member']['mid']
                comment['sex'] = item['member']['sex']
                comment['text'] = item['content']['message']
                comment['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['ctime']))
                comment['likes'] = item['like']
                #comment['ip'] = item['reply_control']['location']
                yield comment
            self.offset += 1
            time.sleep(0.2)
            yield scrapy.Request(self.url.format(self.offset,self.aid), callback = self.parse)
        else:
            pass
        

        
       

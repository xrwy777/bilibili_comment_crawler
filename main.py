import os
import sys
sys.path.append('bilibili')
url = ''
url = str(input("请输入要爬取的网址(输入q退出)："))
if url != 'q':
    os.system("scrapy runspider ./bilibili/spiders/comment.py ")
    

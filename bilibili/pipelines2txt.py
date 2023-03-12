# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import time

class MyscrapyPipeline:

    # 创建构造方法（创建一个存放数据的文件夹）
    def __init__(self):
        # 创建文件夹
        self.folderName = 'output'
        # 判断文件夹是否存在
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)

    # 用process_item函数来处理每一个采集到的电影数据
    def process_item(self, item, spider):
        print("--> TXT : write to text file…………")
        # 获得系统时间
        now = time.strftime('%Y-%m-%d', time.localtime())
        # 设置文件名称
        txtFilename = 'bilibili_' + now + '.txt'
        # 进行文件的写入操作
        try:
            with open(self.folderName + os.sep + txtFilename, 'a') as fp:
                # 写入相关数据
                fp.write('用户名：{0}'.format(item['name']) + '\n')
                fp.write('uid：{0}'.format(item['uid']) + '\n')
                fp.write('性别：{0}'.format(item['sex']) + '\n')
                fp.write('评论：{0}'.format(item['text']) + '\n')
                fp.write('评论时间：{0}'.format(item['time']) + '\n')
                fp.write('点赞数：{0}'.format(item['likes']) + '\n')
                pass
        except IOError as err:
            # 输出相关的报错
            raise ("Txt File Error: " + str(err))
        finally:
            # 关闭文件
            fp.close()
        return item
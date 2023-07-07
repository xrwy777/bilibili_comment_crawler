# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# python对于Excel的操作需要用到第三方模块；
# xlwt：实现对Excel的写入操作；（pip install xlwt）
# xlrd：实现对Excel的读取操作；（pip install xlrd）
# xlutils：使用Excel工具包实现对副本的copy；（pip install xlutils）
from itemadapter import ItemAdapter
import os
import time
import xlwt
import xlrd
from xlutils.copy import copy
from spiders.comment import title

class MyscrapyPipeline:

    # 创建构造方法（创建一个存放数据的文件夹）
    def __init__(self):
        # 创建文件夹
        self.folderName = 'output'
        # 判断文件夹是否存在
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)
        
        # 创建Excel文件
        # 获取当前系统时间
        now = time.strftime('%Y-%m-%d-%H', time.localtime())
        # 设置文件名称
        print(title)
        excelFileName = title + ' ' + now + '.xls'
        self.excelFileName = excelFileName
        print(excelFileName)
        # 获得最终文件路径
        self.excelPath = self.folderName + os.sep + excelFileName
        # 创建工作薄
        self.workbood = xlwt.Workbook(encoding='utf-8')
        # 创建工作页
        self.sheet = self.workbood.add_sheet('b站评论')
        # 写入表头数据项
        headers = ['用户名','uid','性别','评论','评论时间','点赞数']
        # 设置表头数据项的样式
        headerstyls = xlwt.easyxf('font: color-index black, bold on')
        # 使用for循环完成表头数据项的写入
        for i in range(len(headers)):
            self.sheet.write(0,i,headers[i],headerstyls)
            pass
        # 保存Excel数据文件；
        self.workbood.save(self.excelPath)
        # 设置一个写入数据的起始行数（全局变量）
        self.rowindex = 1
        pass

    # 用process_item函数来处理每一个采集到的电影数据
    def process_item(self, item, spider):
        print("--> Excel : write to excel file…………")
        # 读取已经创建好的数据表格，并打开(读取时保持现有格式)
        oldwb = xlrd.open_workbook(self.excelPath, formatting_info=True)
        # copy一个副本文件
        newwb = copy(oldwb)
        # 获取要操作的工作页
        sheet = newwb.get_sheet(0)
        # 获取一个要写入数据项的列表
        itemlist = [item['name'],item['uid'],item['sex'],item['text'],item['time'],item['likes']]
        # 使用for循环完成数据项的写入
        for colindex in range(len(item)):
            sheet.write(self.rowindex,colindex,itemlist[colindex])
            pass
        # 保存Excel数据文件
        newwb.save(self.excelPath)
        # 行数自增1
        self.rowindex += 1
        return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BilibiliPipeline:
    def process_item(self, item, spider):
        print('用户名：{0}'.format(item['name']))
        print('uid：{0}'.format(item['uid']))
        print('性别：{0}'.format(item['sex']))
        print('评论：{0}'.format(item['text']))
        print('评论时间：{0}'.format(item['time']))
        print('点赞数：{0}'.format(item['likes']))
        return item

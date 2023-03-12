# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()#用户名
    sex = scrapy.Field()#性别
    text = scrapy.Field()#评论内容
    time = scrapy.Field()#评论时间
    likes = scrapy.Field()#点赞数
    uid = scrapy.Field()#uid
    #ip = scrapy.Field()#ip属地
    #replys = scrapy.Field()#回复数
    pass

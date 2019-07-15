# -*- coding: utf-8 -*-
import scrapy


class JdCommentsSpider(scrapy.Spider):
    # 定义spider的名称
    name = 'jd_comments'
    # 定义该Spider 允许爬虫的域名
    allowed_domains = ['jd.com']
    # 定义该spider爬取的首页列表
    start_urls = ['https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1465&productId=42217334747&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1']
    #
    def parse(self, response):

        item = JdspiderItem()

        r_json_str = response.text[26:-2]

        r_json_obj = json.loads(r_json_str)

        r_json_comments = r_json_obj['comments']

        for r_json_comment in r_json_comments :

            item['comment'] = r_json_comment[content]

        yield item

'''
        for i in range(1,100):

            # new_link = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1465&productId=42217334747&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%i
            # 截取字符串,让page每次+1.

            yield scrapy.Request(new_link, callback=self.parse)

'''



'''
            with open(COMMENT_FILE_PATH,'a+') as file :

                file.write(r_json_comment['content']+"\n")

                print(r_json_comment['content'])
'''

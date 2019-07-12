# -*- coding: utf-8 -*-
import scrapy


class JdCommentsSpider(scrapy.Spider):
    name = 'jd_comments'
    allowed_domains = ['jd.com']
    start_urls = ['https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1465&productId=42217334747&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1']

    def parse(self, response):
        

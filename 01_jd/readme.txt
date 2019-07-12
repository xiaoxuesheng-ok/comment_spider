01_jd_comments.py
#使用直接解析地址的方式写

'''
1. 打开京东随意选择一个商品，右键检查->network，点击评论页，随意复制一个评论，ctrl+F,回车，一般就可以找到对应的地址了。
2. 先 打印r.text 看看是否正常。
3. 在1的基础上，看一下chrome就可以找到结构了。

'''

02_jd_commentsBySelenium .py
#使用selenium的方式写

03-jdSpiderByScrapy
# 使用框架+使用直接解析地址的方式写

'''

1. scrapy startproject jdSpider ,创建文件夹

2. 在命令行窗口中进入 spiders 目录下，然后执行如下命令即可创建一个 Spider：
  scrapy genspider jd_comments  "jd.com"

3. 打开京东随意选择一个商品，右键检查->network，点击评论页，随意复制一个评论，ctrl+F,回车，一般就可以找到对应的地址了。

4. 然后把地址复制到start_urls，作为起始地址。

5.

'''

04_
# 使用框架+使用selenium的方式写

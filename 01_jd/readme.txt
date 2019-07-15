01_jd_comments.py
#使用直接解析地址的方式写

'''
1. 打开京东随意选择一个商品，右键检查->network，点击评论页，随意复制一个评论，ctrl+F,回车，一般就可以找到对应的地址了。
2. 先 打印r.text 看看是否正常。
3. 在1的基础上，看一下chrome就可以找到结构了。

'''

02_jd_commentsBySelenium .py
#使用selenium的方式写
# 可以使用xml和CSS,还可以用beautiful的


03-jdSpiderByScrapy
# 使用框架+使用直接解析地址的方式写

'''

1. scrapy startproject jdSpider ,创建文件夹

2. 在命令行窗口中进入 spiders 目录下，然后执行如下命令即可创建一个 Spider：
  scrapy genspider jd_comments  "jd.com"

3. 编写items.

4. 打开京东随意选择一个商品，右键检查->network，点击评论页，随意复制一个评论，ctrl+F,回车，一般就可以找到对应的地址了。
一般动态加载的数据都以json形式存储，在Filter里填json过滤，可以更加快速地寻找到想要的文件，但不是所有的网站都适用，还是需要在JS或XHR里手动寻找所需文件。

4. 然后把地址复制到start_urls，作为起始地址。

5. parse 方法,返回的response, 就是平常请求到的页面内容.不管是html,JSON,该怎么处理就怎么处理.

6. pipelines.py 文件


7. settings.py

# 配置默认的请求头
DEFAULT_REQUEST_HEADERS = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
# 配置使用Pipeline
ITEM_PIPELINES = {
    'ZhipinSpider.pipelines.ZhipinspiderPipeline': 300,
}


'''

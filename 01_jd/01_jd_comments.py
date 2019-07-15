import os
import time
import json
import random
import requests







COMMENT_FILE_PATH = '01_jd_comment.txt'


def spider_comment(page = 0):
    '''
    爬取京东指定页评论数据
    param： page  # 爬取第几，默认值为0
    '''

    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1465&productId=42217334747&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1" %page

    header = {
    'User-Agent': 'Mozilla/5.0' ,
    'Referer' : 'https://item.jd.com/42217334747.html'
    }


    try :
        r = requests.get(url,headers = header)
        r.raise_for_status()
    except :
        print("爬取失败")

    #print(r.text)

    r_json_str = r.text[26:-2]

    r_json_obj = json.loads(r_json_str)

    r_json_comments = r_json_obj['comments']

    for r_json_comment in r_json_comments :

        with open(COMMENT_FILE_PATH,'a+') as file :

            file.write(r_json_comment['content']+"\n")

            print(r_json_comment['content'])


def  batch_spider_comment():
    '''
    批量抓取评论
    '''
    if os.path.exists(COMMENT_FILE_PATH) :
        os.remove(COMMENT_FILE_PATH)

    for i in range(100):
        spider_comment(i)
        time.sleep(random.random()*5)







if __name__ == '__main__':

    create_word_cloud()

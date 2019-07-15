from selenium import webdriver
from lxml import etree
import os
import time
import random

COMMENT_FILE_PATH = '02_jd_commentsBySelenium.txt'


# 有头模式
#driver = webdriver.Firefox()

#无头模式
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)


driver.get("https://item.jd.com/42217334747.html#comment")
time.sleep(random.random()*5)


'''
# @1，直接选择器

if os.path.exists(COMMENT_FILE_PATH) :
    os.remove(COMMENT_FILE_PATH)

for i in range(1,100) :

    time.sleep(random.random()*5)

    if i != 1 :

        driver.find_element_by_css_selector('a.ui-pager-next').click()

    comments = driver.find_elements_by_css_selector('p.comment-con')

    for  eachcomment  in comments :

        with open(COMMENT_FILE_PATH,'a+') as file :

            file.write(eachcomment.text+"\n")

            print(eachcomment.text)

'''


'''
# @2，直接XPATH
'''

if os.path.exists(COMMENT_FILE_PATH) :
    os.remove(COMMENT_FILE_PATH)

for i in range(1,100) :

    time.sleep(random.random()*5)

    if i != 1 :

        driver.find_element_by_css_selector('a.ui-pager-next').click()

    for i in range(1,10):

        if i <= 10 :

            eachcomment = driver.find_element_by_xpath('//*[@id="comment-0"]/div['+str(i)+']/div[2]/p')

            with open(COMMENT_FILE_PATH,'a+') as file :

                file.write(eachcomment.text+"\n")

                print(eachcomment.text)



'''
# @3，转换为lxml后,XPATH

if os.path.exists(COMMENT_FILE_PATH) :
    os.remove(COMMENT_FILE_PATH)

res = driver.page_source

rs1 = etree.HTML(res)

for i in range(1,100) :

    time.sleep(random.random()*5)

    if i != 1 :

        driver.find_element_by_css_selector('a.ui-pager-next').click()

    for i in range(1,10):

        if i <= 10 :

            with open(COMMENT_FILE_PATH,'a+') as file :

                file.write(rs1.xpath('//*[@id="comment-0"]/div['+str(i)+']/div[2]/p/text()')+"\n")

                print(rs1.xpath('//*[@id="comment-0"]/div['+str(i)+']/div[2]/p/text()'))
'''


'''
# @4 Beautiful, 放弃.
'''

driver.close()

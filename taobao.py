from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from get_products import getpro
from total_page import total
import time
browser = webdriver.Chrome(executable_path = '/Users/xiaopeng/Downloads/chromedriver')
wait = WebDriverWait(browser,10)
def index_page(page):
    '''
    抓取索引页
    :param page:页码
    :return:
    '''
    print('正在爬取',page,'页')
    try:
        url = 'http://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url)
        if page>1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        #判断节点是否包含文字
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        print('OK')
        getpro(browser,KEYWORD)
    except TimeoutException as e:
        print(e)
        index_page(page)
if __name__ == '__main__':
    KEYWORD = input('请输入商品名称\n')
    url = 'http://s.taobao.com/search?q=' + quote(KEYWORD)
    browser.get(url)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        pagenum = total(browser)
    except:
        pagenum = 1
    while(True):
        pagelength = input('请输入爬取页数\n')
        if(int(pagelength)<pagenum):
            break
    for i in range(1,int(pagelength)+1):
        index_page(i)
    browser.close()
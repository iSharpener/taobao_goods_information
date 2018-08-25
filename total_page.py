from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import re
def total(browser):
    try:
        html = browser.page_source
        soup = BeautifulSoup(html,'lxml')
        total = soup.select('#mainsrp-pager > div > div > div > div.total')
        text = total[0].get_text()
        # print(text)
        result = re.search('^.*?([1-9]\d*|0).*?$',text,re.S)
        print('总页数为'+result.group(1)+'页')
        return int(result.group(1))
    except:
        return 1
from pyquery import PyQuery as pq
from save import save_to_mongo
import hashlib
import requests
def getpro(browser,keyword):
    '''
    获取商品数据
    :return:
    '''
    originpath = '/Users/xiaopeng/Pictures/淘宝商品/'
    html = browser.page_source
    doc = pq(html)
    #选择id为mainsrp-itemlist的元素中class为items下的所有class为item的元素，通过items()返回一个迭代器
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.row.row-2.title .J_ClickStat').text().replace('\n',''),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        try:
            product['image'] = 'http://'+item.find('.pic .img').attr('data-src').replace('//','')
        except:
            product['image'] = 'None'
        print(product['image'])
        m1 = hashlib.md5()
        m1.update(product['image'].encode('utf-8'))
        print(m1.hexdigest())
        try:
            wholepath = originpath+m1.hexdigest()+'.jpg'
            print("正在下载到"+wholepath)
            with open(wholepath,'wb') as f:
                f.write(requests.get(product['image'],timeout=5).content)
            print("下载成功")
        except Exception as e:
            print(e)
            print("没有图片")
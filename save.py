from pypinyin import  pinyin,lazy_pinyin
import pymongo
MONGO_URL = 'localhost'
MONGO_DB = 'tabaodata'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def save_to_mongo(product,keyword):
    '''
    将字典类型的数据保存带mongo数据库
    :param product:
    :return:
    '''

    MONGO_COLLECTION = ''.join(lazy_pinyin(keyword))
    try:
        if db[MONGO_COLLECTION].insert(product):
            print(product['title']+'  存储到数据库成功')
    except Exception as e:
        print(e)
        print(product['title']+'  存储到数据库失败')
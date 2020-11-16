import requests                     # requests 用来爬取页面
import logging                      # logging 用来输出信息
import re                           # re 用来实现正则表达式解析
import pymongo                      # pymongo 用来实现 MongoDB 存储
from pyquery import PyQuery as pq   # pyquery 用来直接解析网页
from urllib.parse import urljoin    # urljoin 用来做 URL 的拼接
import multiprocessing              # 多线程加速

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')  # 定义日志输出级别和输出格式
BASE_URL = 'https://static1.scrape.cuiqingcai.com'      # BASE_URL 为当前站点的根 URL
TOTAL_PAGE = 10      # TOTAL_PAGE 为需要爬取的总页码数量

# MongoDB 的连接配置
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'   # MongoDB 数据库的名称
MONGO_COLLECTION_NAME = 'movies'   # MongoDB 的集合名称
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']

# 实现一个页面爬取的方法
def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)  # 将 logging 的 error 方法的 exc_info 参数设置为 True 则可以打印出 Traceback 错误堆栈信息

# 定义列表页的爬取方法
def scrape_index(page):
    # 接收一个 page 参数，即列表页的页码
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

# 解析列表页，并得到每部电影的详情页的 URL
def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info('get detail url %s', detail_url)
        yield detail_url

# 整合
# def main():
#     for page in range(1, TOTAL_PAGE + 1):
#         index_html = scrape_index(page)
#         detail_urls = parse_index(index_html)
#         logging.info('detail urls %s', list(detail_urls))


# 爬取详情页
def scrape_detail(url):
    return scrape_page(url)

# 详情页的解析
def parse_detail(html):
    doc = pq(html)
    cover = doc('img.cover').attr('src')   # 封面，直接选取 class 为 cover 的 img 节点，并调用 attr 方法获取 src 属性的内容
    name = doc('a > h2').text()   # 获取详情页中的电影名称选取 a 节点的直接子节点 h2 节点，并调用 text 方法提取其文本内容
    categories = [item.text() for item in doc('.categories button span').items()]  # 类别，有多个，需要遍历
    published_at = doc('.info:contains(上映)').text()   # pyquery 支持使用 :contains 直接指定包含的文本内容并进行提取，且每个上映时间信息都包含了「上映」二字，所以我们这里就直接使用 :contains(上映) 提取了 class 为 info 的 div 节点
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None   # 调用正则表达式把日期单独提取出来
    drama = doc('.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None  # 转成浮点数
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }

# 改写main方法
# def main():
#     for page in range(1, TOTAL_PAGE + 1):
#         index_html = scrape_index(page)
#         detail_urls = parse_index(index_html)
#         for detail_url in detail_urls:
#             detail_html = scrape_detail(detail_url)
#             data = parse_detail(detail_html)
#             logging.info('get detail data %s', data)

# 成功提取到详情页信息之后，将数据存储到MongoDB数据库中
# 确保现在有一个可以正常连接和使用的 MongoDB 数据库

# 将数据保存到 MongoDB的方法
def save_data(data):
    collection.update_one({'name': data.get('name')}, {'$set': data}, upsert=True)
    # 调用了update_one方法:
        # 第 1 个参数是查询条件，即根据 name 进行查询
        # 第 2 个参数是 data 对象本身，也就是所有的数据，这里我们用 $set 操作符表示更新操作
        # 第 3 个参数很关键，这里实际上是 upsert 参数，如果把这个设置为 True，则可以做到存在即更新，不存在即插入的功能，更新会根据第一个参数设置的 name 字段，所以这样可以防止数据库中出现同名的电影数据

# 改写main方法
# def main():
#     for page in range(1, TOTAL_PAGE + 1):
#         index_html = scrape_index(page)
#         detail_urls = parse_index(index_html)
#         for detail_url in detail_urls:
#             detail_html = scrape_detail(detail_url)
#             data = parse_detail(detail_html)
#             logging.info('get detail data %s', data)
#             logging.info('saving data to mongodb')
#             save_data(data)
#             logging.info('data saved successfully')

# 多进程加速
# 由于一共有 10 页详情页，并且这 10 页内容是互不干扰的，所以我们可以一页开一个进程来爬取。
# 由于这 10 个列表页页码正好可以提前构造成一个列表，所以我们可以选用多进程里面的进程池 Pool 来实现这个过程。

# 修改main方法
# import multiprocessing

def main(page):
    # 添加一个参数 page，用以表示列表页的页码
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to mongodb')
        save_data(data)
        logging.info('data saved successfully')





if __name__ == '__main__':

    # main()  # 抓取详情页信息并保存到数据库

    # 多进程加速
    pool = multiprocessing.Pool()  # 声明一个进程池
    pages = range(1, TOTAL_PAGE + 1)  # 声明 pages 为所有需要遍历的页码，即 1~10
    pool.map(main, pages)  # 调用 map 方法，第 1 个参数就是需要被调用的方法，第 2 个参数就是 pages，即需要遍历的页码
    pool.close()
    pool.join()

    # 把 1~10 这 10 个页码分别传递给 main 方法，并把每次的调用变成一个进程，加入到进程池中执行，
    # 进程池会根据当前运行环境来决定运行多少进程。
    # 比如我的机器的 CPU 有 8 个核，那么进程池的大小会默认设定为 8，这样就会同时有 8 个进程并行执行


# 爬取目标： https://dynamic1.scrape.cuiqingcai.com/
# 需要爬取的数据包括电影的名称、封面、类别、上映日期、评分、剧情简介等信息


# 直接获取页面,分析Ajax接口逻辑
# import requests
#
# url = 'https://dynamic1.scrape.cuiqingcai.com/'
# html = requests.get(url).text
# print(html)  # 得到的是JS和一些CSS，说明最终整个页面的展示是通过发送ajax数据，JS渲染出来的

import requests
import logging

import json
from os import makedirs
from os.path import exists

# 基本配置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/?limit={limit}&offset={offset}'  # 把 limit 和 offset 预留出来变成占位符，可以动态传入参数构造成一个完整的列表页 URL

# 列表页的爬取
# 一个通用的爬取方法
def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # 解析响应的内容并将其转化成 JSON 字符串
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 爬取列表页的方法
LIMIT = 10
def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

# 由于这时爬取到的数据已经是 JSON 类型了，所以我们不用像之前一样去解析 HTML 代码来提取数据，
# 爬到的数据就是我们想要的结构化数据，因此解析这一步这里我们就可以直接省略啦。

# 爬取详情页
DETAIL_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/{id}'
def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

# 总的调用逻辑
TOTAL_PAGE = 10
# def main():
#     for page in range(1, TOTAL_PAGE + 1):
#         index_data = scrape_index(page)
#         for item in index_data.get('results'):
#             id = item.get('id')
#             detail_data = scrape_detail(id)
#             logging.info('detail data %s', detail_data)

# 保存数据
RESULTS_DIR = 'results'  # 定义数据保存的文件夹 RESULTS_DIR
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)  # 先要判断这个文件夹是否存在，如果不存在则需要创建。
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'  # 电影名称作为 JSON 文件的名称
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)  # 用 json 的 dump 方法将数据保存成文本格式
    # 两个参数
        # 一个是 ensure_ascii，将其设置为 False，它可以保证中文字符在文件中能以正常的中文文本呈现，而不是 unicode 字符
        # 一个是 indent，它的数值为 2，这代表生成的 JSON 数据结果有两个空格缩进

# 调整main方法
def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)

# 由于 Ajax 接口大部分返回的是 JSON 数据，所以在一定程度上可以避免一些数据提取的工作，减轻我们的工作量

if __name__ == '__main__':
    main()


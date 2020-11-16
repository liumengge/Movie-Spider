## GET请求

# import requests
# r = requests.get('http://httpbin.org/get')
# print(r.text)


# GET请求时，实现请求参数的拼接
# data = {
#     'name': 'germey',
#     'age': 25
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)


# r = requests.get('http://httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json())) # 调用 json 方法，就可以将返回结果是 JSON 格式的字符串转化为字典

# 需要注意的是，如果返回结果不是 JSON 格式，便会出现解析错误，抛出 json.decoder.JSONDecodeError 异常

# 抓取网页
# import requests
# import re
# r = requests.get('https://static1.scrape.cuiqingcai.com/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)   # 正则表达式匹配到所有的标题
# titles = re.findall(pattern, r.text)
# print(titles)

# 抓取二进制数据：抓取图片/音频/视频等文件
# 抓取github站点图标
# import requests
# r = requests.get('https://github.com/favicon.ico')
# # Response 对象的两个属性
# print(r.text)  # 由于图片是二进制数据，在打印时转化为 str 类型，也就是图片直接转化为字符串，出现乱码
# print(r.content)  # 前面带有一个b，表示是bytes类型的数据

# 将抓取到的图标保存下来
# import requests
# r = requests.get('https://github.com/favicon.ico')
# with open('./images/favicon.ico', 'wb') as f:
#     f.write(r.content)

# 添加请求头Request Headers信息，如果不添加很容易被当成是异常请求
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

r = requests.get('https://static1.scrape.cuiqingcai.com/', headers=headers)
print(r.text)


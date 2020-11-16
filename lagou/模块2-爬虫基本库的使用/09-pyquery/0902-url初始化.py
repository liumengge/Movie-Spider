# from pyquery import PyQuery as pq
#
# doc = pq(url='https://cuiqingcai.com')
# # pyquery 对象会首先请求这个 URL，然后用得到的 HTML 内容完成初始化。这就相当于将网页的源代码以字符串的形式传递给 pyquery 类来初始化。
# print(doc('title'))


# 上述代码与以下代码含义是相同的
# from pyquery import PyQuery as pq
# import requests
#
# doc = pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))

# 文件初始化
from pyquery import PyQuery as pq

doc = pq(filename='demo.html')
print(doc('li'))

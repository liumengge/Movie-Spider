# 基本实现

# import requests
# data = {'name': 'germey', 'age': '25'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text) # form 部分就是提交的数据

# 在上面的实例中，我们使用 text 和 content 获取了响应的内容。此外，还有很多属性和方法可以用来获取其他信息，比如状态码、响应头、Cookies 等
# import requests
# r = requests.get('https://static1.scrape.cuiqingcai.com/')
# print(type(r.status_code), r.status_code) # 以通过判断 Response 的状态码来确认是否爬取成功。
# print(type(r.headers), r.headers)  # 获取响应头
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history) # 请求历史


# requests 还提供了一个内置的状态码查询对象 requests.codes
import requests
r = requests.get('https://static1.scrape.cuiqingcai.com/')
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')




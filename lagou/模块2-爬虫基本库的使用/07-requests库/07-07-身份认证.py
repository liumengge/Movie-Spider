# 有登陆窗口
# HTTP Basic Access Authentication，它是一种用来允许网页浏览器或其他客户端程序在请求时提供用户名和口令形式的身份凭证的一种登录验证方式。

# 我们可以使用 requests 自带的身份认证功能，通过 auth 参数即可设置
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://static3.scrape.cuiqingcai.com/', auth=HTTPBasicAuth('admin', 'admin'))  # 这个示例网站的用户名和密码都是 admin，在这里我们可以直接设置
# 如果用户名和密码正确的话，请求时会自动认证成功，返回 200 状态码；如果认证失败，则返回 401 状态码

r = requests.get('https://static3.scrape.cuiqingcai.com/', auth=('admin', 'admin'))

print(r.status_code)

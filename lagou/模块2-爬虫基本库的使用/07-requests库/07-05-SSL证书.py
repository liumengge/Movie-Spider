# 在浏览器中通过一些设置来忽略证书的验证
# import requests
# response = requests.get('https://static2.scrape.cuiqingcai.com/')
# print(response.status_code)   # 直接抛出了 SSLError 错误，原因就是因为我们请求的 URL 的证书是无效的

# 可以使用 verify 参数控制是否验证证书，如果将其设置为 False，在请求时就不会再验证证书是否有效。如果不加 verify 参数的话，默认值是 True，会自动验证。
# import requests
# response = requests.get('https://static2.scrape.cuiqingcai.com/', verify=False)
# print(response.status_code)

# 我们可以通过设置忽略警告的方式来屏蔽这个警告：
import requests
from requests.packages import urllib3

# urllib3.disable_warnings()
# response = requests.get('https://static2.scrape.cuiqingcai.com/', verify=False)
# print(response.status_code)

# 或者通过捕获警告到日志的方式忽略警告
import logging
import requests

logging.captureWarnings(True)
response = requests.get('https://static2.scrape.cuiqingcai.com/', verify=False)
print(response.status_code)



# import requests
# requests.get('http://httpbin.org/cookies/set/number/123456789')  # 请求这个网址时，可以设置一个 cookie，名称叫作 number，内容是 123456789
# r = requests.get('http://httpbin.org/cookies')  # 请求了 http://httpbin.org/cookies，此网址可以获取当前的 Cookies
# print(r.text)  # 获取不到


# 用 Session：
import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

# 利用 Session，可以做到模拟同一个 Session 而不用担心 Cookies 的问题。它通常用于模拟登录成功之后再进行下一步的操作。

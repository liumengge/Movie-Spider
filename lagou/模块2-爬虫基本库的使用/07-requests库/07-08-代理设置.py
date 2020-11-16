# 某些网站在测试的时候请求几次，能正常获取内容。但是对于大规模且频繁的请求，
# 网站可能会弹出验证码，或者跳转到登录认证页面，更甚者可能会直接封禁客户端的 IP，导致一定时间段内无法访问。

# import requests
# proxies = {
#   'http': 'http://10.10.10.10:1080',
#   'https': 'http://10.10.10.10:1080',
# }
# requests.get('https://httpbin.org/get', proxies=proxies)



# 若代理需要使用身份认证
import requests
proxies = {'https': 'http://user:password@10.10.10.10:1080/',}
requests.get('https://httpbin.org/get', proxies=proxies)



# requests 还支持 SOCKS 协议的代理
import requests
proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get('https://httpbin.org/get', proxies=proxies)





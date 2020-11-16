import requests

r = requests.get('https://httpbin.org/get', timeout=1)  # timeout参数默认值是None，表示永久等待
print(r.status_code)

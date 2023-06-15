import requests
import socket

url ='https://www.sehuatang.org/forum-36-1.html'
# url ='http://www.baidu.com'


headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# proxies = {'http': "socks://127.0.0.1:10808",
#            'https': "socks://127.0.0.1:10808"}
#设置代理
proxy = '127.0.0.1:10809'
proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy,
}

response = requests.get(url=url,headers=headers,proxies=proxies)
print(response.text)

# try:
#     response = requests.get(url=url,headers=headers,proxies=proxies,)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)

# response = requests.get(url=url,headers=headers,proxies=proxy)

# print(response.text)


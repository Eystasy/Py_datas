import requests
from fake_useragent import UserAgent

# url = 'https://www.google.com/'
url = 'https://www.b9m4w.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 115Browser/25.0.6.5'
}

# proxy={'http':'http://127.0.0.1:10809','https':'https://127.0.0.1:10809'}

res = requests.get(url=url,headers=headers,verify=False)
# requests.get()
print(res.status_code)
print(res.text)
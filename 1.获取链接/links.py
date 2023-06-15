import requests
from fake_useragent import UserAgent
from lxml import etree
import time


# headers = {
#     'User-Agent':UserAgent().random
# }

# url= input('请输入你要下载的网页，按回车开始下载 0.0')
url = 'https://www.sehuatang.net/forum-36-1.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

proxies = {'http': "socks5://127.0.0.1:10808",
           'https': "socks5://127.0.0.1:10808"}

def main():
    response = requests.get(url=url, headers=headers,proxies=proxies)
    e = etree.HTML(response.text)
    title = e.xpath('//th//a[@class="s xst"]/text()')
    urls = e.xpath('//th//a[@class="s xst"]/@href')
    with ThreadPoolExecutor(20) as t:
        for urla in urls:
            r_url = 'https://www.sehuatang.org/'+urla
            resp =requests.get(url=r_url,headers=headers,proxies=proxies)
            b = etree.HTML(resp.text)
            # names = b.xpath('//span[@id="thread_subject"]/text()') #获取影片名字
            mag = b.xpath('//div[@class="blockcode"]//li/text()') #获取磁力
            # print(names[0])
            for i in mag:
                with open('magnet.txt','a+',encoding='utf-8') as q:
                    q.write(str(i)+'\n')
                    print('正在下载:',i)


input('下载完毕，按任意键即可退出')
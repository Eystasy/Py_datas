import requests
import time
from fake_useragent import UserAgent
from lxml import etree

base_url ='https://www.b9m4w.com/'
# url = 'https://www.b9m4w.com/forum-36-1.html'
# # url = 'https://iweec.com/'

headers = {
    "User-Agent":UserAgent().random
}

cookie = {
    'cookie':'cPNj_2132_saltkey=ZSAQkjsg; _ga=GA1.1.332088905.1683274637; _ga_6MTS3NVM0T=GS1.1.1683274637.1.1.1683274637.0.0.0; _safe=vqd37pjm4p5uodq339yzk6b7jdt6oich'
}
def main(url):
    try:
        response = requests.get(url=url,headers=headers,cookies=cookie)
        e = etree.HTML(response.text)
        title = e.xpath('//th//a[@class="s xst"]/text()')
        urls = e.xpath('//th//a[@class="s xst"]/@href')
        for s_url in urls:
            real_url = base_url + s_url
            res = requests.get(url=real_url,headers=headers,cookies=cookie)
            e_1 = etree.HTML(res.text)
            title = e_1.xpath('//h1/span/text()') #获取影片名字
            magnet = e_1.xpath('//ol/li/text()') #获取磁力链接
            # pic = e_1.xpath('//table[@class="plhin"]//div[@class="pcb"]//img/@src') #获取图片链接
            for i in magnet:
                with open('magnet.txt', 'a+', encoding='utf-8') as q:
                    q.write(str(i) + '\n')
                    print('正在下载--------:', i)
            time.sleep(0.5)
        # print(title)
        # print(urls)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)

if __name__ == '__main__':
    start = print('-----------------欢迎使用磁力下载系统-----------------')
    start = 1
    while start == 1:
        print('------板块编码查询------\n 2.国产原创\n 36.亚洲无码原创\n 37.亚洲有码原创\n 103.高清中文字幕\n 107.三级写真\n 160.VR视频区\n 104.素人有码系列\n 38.欧美无码\n 151.4K原版\n 152.韩国主播\n 39.动漫原创')
        ls = input('您好，请输入板块编号，按回车确认：')
        num1 = input('请输入开始的页码，按回车确认：')
        num2 = input('请输入结尾的页码，按回车确认：')
        for num in range(int(num1), int(num2) + 1):
            url = f"https://www.b9m4w.com/forum-{ls}-{num}.html"
            main(url)
        input('恭喜您！磁力获取完毕！\n 1、退出下载请按Ctrl+C \n 2、按任意键继续下载......')
    else:
        input('确认退出按回车键！')
    input('确认退出按回车键！')
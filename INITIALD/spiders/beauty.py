#抓取美女汽车相关信息
import scrapy
import re
import requests
from bs4 import BeautifulSoup
from INITIALD.items import ForumItem


class Beauty(scrapy.Spider):
    name = "beauty"
    download_delay = 1
    allowed_domains = ["autohome.com.cn"]


    urls = [
        "https://club.autohome.com.cn/JingXuan/104/",
        "https://club.autohome.com.cn/JingXuan/292/",
        "https://club.autohome.com.cn/JingXuan/172/",
        "https://club.autohome.com.cn/JingXuan/349/",
        "https://club.autohome.com.cn/JingXuan/291/",
        "https://club.autohome.com.cn/JingXuan/272/",
        "https://club.autohome.com.cn/JingXuan/275/",
        "https://club.autohome.com.cn/JingXuan/276/",
        "https://club.autohome.com.cn/JingXuan/106/",
        "https://club.autohome.com.cn/JingXuan/277/",
        "https://club.autohome.com.cn/JingXuan/278/",
        "https://club.autohome.com.cn/JingXuan/279/",
        "https://club.autohome.com.cn/JingXuan/295/",
        "https://club.autohome.com.cn/JingXuan/293/",
        "https://club.autohome.com.cn/JingXuan/280/",
        "https://club.autohome.com.cn/JingXuan/294/",
        "https://club.autohome.com.cn/JingXuan/168/",
        "https://club.autohome.com.cn/JingXuan/326/",
        "https://club.autohome.com.cn/JingXuan/107/",
        "https://club.autohome.com.cn/JingXuan/122/",
        "https://club.autohome.com.cn/JingXuan/119/",
        "https://club.autohome.com.cn/JingXuan/261/",
        "https://club.autohome.com.cn/JingXuan/282/"
    ]
    start_urls = []

    for url in urls:
        #获取总共的页码
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html,'lxml')
        fs = soup.select('.fs')[0].text
        count = int(re.sub("\D", "", fs))
        for i in range(1,count + 1):
            start_urls.append(url + str(i))

    def parse(self,response):
        items = []
        keywords = response.css('meta::attr(content)')[1].extract()
        keyword = keywords.split(',')[0]
        contents = response.css('.content li')
        for content in contents:
            pic_box = content.css('div.pic-box')
            url = "https:" + pic_box.css('a::attr(href)').extract_first()
            pic_url = "https:" + pic_box.css('img::attr(data-original)').extract_first()
            title = pic_box.css('a::attr(title)').extract_first()
            bea = ForumItem()
            bea['title'] = title
            bea['url'] = url
            bea['img'] = pic_url
            bea['keyword'] = keyword
            items.append(bea)
        return items

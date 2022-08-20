
import scrapy
from ..items import NewsSpidersItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = ['https://www.indiatoday.in/top-stories']

    def parse(self,response):
        for i in  response.css('div.catagory-listing'):
            news = NewsSpidersItem()
            heading = i.css('div.detail h2').attrib['title']
            img = i.css('div.pic img').attrib['src']
            url = "https://www.indiatoday.in" +i.css('div.detail a').attrib['href']

            news["heading"] = heading
            news["img"] = img
            news['url'] = url
            yield news

        next_page = "https://www.indiatoday.in" + response.css("li.pager-next a").attrib['href']   
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)                     
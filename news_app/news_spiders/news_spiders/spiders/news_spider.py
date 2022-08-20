
import scrapy
from ..items import NewsSpidersItem
import requests
from bs4 import BeautifulSoup

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
            news['content'] = self.scarp_p_tag_content(news['url'])
            yield news

        next_page = "https://www.indiatoday.in" + response.css("li.pager-next a").attrib['href']   
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)                     

    def scarp_p_tag_content(self,url):
    # yield response.css('div.description p')
        res = ""
            
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")  
        desc = soup.find('div',class_ = "description")
        p_tag = desc.find_all('p')
        for i in p_tag:
            res += i.text
        return res        
#引入文件
import scrapy
#引入容器
from movie.CourseItems import Courseitem

class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]
    def parse(self,response):
        #实例化容器
        item = Courseitem()
        for box in response.xpath('//div[@class="item"]'):
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            item['url'] =  box.xpath('.//a/@href').extract()[0]
            item['title'] = box.xpath('.//span[@class="title"]/text()').extract()[0]
            item['score'] = box.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            item['image_url'] = box.xpath('.//@src').extract()[0]
            yield item
        #url跟进
        url = response.xpath("//a[contains(text(),'后页')]/@href").extract()
        if url:
            page = 'https://movie.douban.com/top250' + url[0]
            yield scrapy.Request(page,callback=self.parse)

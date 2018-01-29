# -*- coding: utf-8 -*-
import scrapy
from tianmao.items import TianmaoItem


class TopgoodSpider(scrapy.Spider):
    name = 'topgood'
    allowed_domains = ['list.tmall.com', 'detail.tmall.com']  # 二级域名

    start_urls = ['https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.4b3df937tMXU1S&cat=50024399&sort=d&style=g&active=1&industryCatId=50024399&theme=663']
    
    def parse(self, response):
        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product item-1111 ']/div")
        print(divs)
        
        for div in divs:
            item = TianmaoItem()
            # 价格
            item['GOODS_PRICE'] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()  # 序列化该节点为unicode字符串并返回list
            print(item)
            # 名称//*[@id="J_ItemList"]/div[3]/div/div[2]/a[1]
            item['GOODS_NAME'] = div.xpath("div[@class='productTitle productTitle-spu']/a[1]/@title")[0].extract()
            print(item)
            pre_Product_Url = div.xpath("div[@class='productTitle productTitle-spu']/a[1]/@href").extract_first()
            
            if 'http' not in pre_Product_Url:
                pre_Product_Url = response.urljoin(pre_Product_Url)
            
            item['GOODS_URL'] = pre_Product_Url
            print(item)
            yield scrapy.Request(url=pre_Product_Url, meta={'item': item}, callback=self.parse_detail,dont_filter=True)

    def parse_detail(self, response):
        divs = response.xpath("//div[@class='extend']/ul")
        
        if len(divs) == 0:
            self.log("Detail Page error --%s"%response.url)
        
        div = divs[0]
        item = response.meta['item']
        item['SHOP_NAME'] = div.xpath("li[1]/div[1]/a/text()")[0].extract().strip()
        item['SHOP_URL'] = div.xpath("li[1]/div[1]/a/@href")[0].extract()
        
        yield item
# 要保存为csv的格式    scrapy crawl topgood -o result.csv
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy


# In[2]:


class BooksSpider(scrapy.Spider):
	name = 'plants'
	allowed_domains = ['toscrape.com/']
	start_urls = ['https://books.toscrape.com/']

	def parse(self, response):
         for container in response.xpath('//article[@class="product_pod"]'):
             image_link = container.xpath('.//div[@class="image_container"]/a/img/@src').get()
             price = container.xpath('.//p[@class="price_color"]/text()').get('').strip()
             link = container.xpath('.//div[@class="image_container"]/a/@href').get()
             title = container.xpath('.//h3/a/text()').get()
             yield {'image_link':image_link,
                    'price':price,
                    'link':link,
                    'title':title}


# In[3]:


from scrapy.crawler import CrawlerProcess


# In[4]:


process = CrawlerProcess(settings = {'FEEDS':{'books.csv':{'format':'csv'}}})
process.crawl(BooksSpider)
process.start()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





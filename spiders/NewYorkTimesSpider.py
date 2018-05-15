#Scraping news articles from the New York Times
#Range of topics stored in the list topics
#The spider starts at http://www.nytimes.com/section/one_of_the_topic_names
#Gets the links to the articles
#Crawls them and gets the entire article text
# -*- coding: utf-8 -*-
import scrapy


class AbcSpider(scrapy.Spider):
    name = 'abc'
    topics= ['politics','business','technology','health','sports']
    start_urls = ['http://www.nytimes.com/section/%s/' % page for page in topics]
    
    def parse(self, response):#Get the links
        SET_SELECTOR= '.story-body'
        for i in response.css(SET_SELECTOR):
            NAME_SELECTOR= 'div a::attr(href)'           
            yield scrapy.Request(i.css(NAME_SELECTOR).extract_first(), callback=self.parse_text)    
    
    def parse_text(self, response): #Get the text
        SET_SELECTOR = '.StoryBodyCompanionColumn'
        for text in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'div ::text'
            yield{'article':text.css(NAME_SELECTOR).extract()}
            
        
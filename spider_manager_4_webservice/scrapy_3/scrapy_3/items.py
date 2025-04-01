# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy3ItemStackOverflow(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question_id = scrapy.Field()
    title = scrapy.Field()
    tag1 = scrapy.Field()
    task_id_p = scrapy.Field()
    spider_p = scrapy.Field()
    ip_p = scrapy.Field()
    docker_id_p = scrapy.Field()
    worker_id_p = scrapy.Field()
    task_id_c = scrapy.Field()
    spider_c = scrapy.Field()
    ip_c = scrapy.Field()
    docker_id_c = scrapy.Field()
    worker_id_c = scrapy.Field()

    pipetype = scrapy.Field()
    detail = scrapy.Field()

class Scrapy3Item_Kaggle_Competition(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()       
    id = scrapy.Field()    
    tag1 = scrapy.Field()
    name = scrapy.Field()
    detail = scrapy.Field()
    task_id_p = scrapy.Field()
    spider_p = scrapy.Field()
    ip_p = scrapy.Field()
    docker_id_p = scrapy.Field()
    worker_id_p = scrapy.Field()
    task_id_c = scrapy.Field()
    spider_c = scrapy.Field()
    ip_c = scrapy.Field()
    docker_id_c = scrapy.Field()
    worker_id_c = scrapy.Field()

    pipetype = scrapy.Field()

class Scrapy3Item_Kaggle_Dataset(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()       
    id = scrapy.Field()    
    url = scrapy.Field()
    tag1 = scrapy.Field()
    detail = scrapy.Field()
    task_id_p = scrapy.Field()
    spider_p = scrapy.Field()
    ip_p = scrapy.Field()
    docker_id_p = scrapy.Field()
    worker_id_p = scrapy.Field()
    task_id_c = scrapy.Field()
    spider_c = scrapy.Field()
    ip_c = scrapy.Field()
    docker_id_c = scrapy.Field()
    worker_id_c = scrapy.Field()

    pipetype = scrapy.Field()  

class Scrapy3Item_Kaggle_Kernel(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()       
    # id = scrapy.Field()    
    competitionId = scrapy.Field()    
    kernelId = scrapy.Field() 
    detail = scrapy.Field()
    tag1 = scrapy.Field()
    task_id_p = scrapy.Field()
    spider_p = scrapy.Field()
    ip_p = scrapy.Field()
    docker_id_p = scrapy.Field()
    worker_id_p = scrapy.Field()
    task_id_c = scrapy.Field()
    spider_c = scrapy.Field()
    ip_c = scrapy.Field()
    docker_id_c = scrapy.Field()
    worker_id_c = scrapy.Field()


    pipetype = scrapy.Field()  



    

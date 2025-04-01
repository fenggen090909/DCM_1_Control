# Define your item pipelines23 here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
from scrapy import signals
from scrapy_3.db.conn_postgres import ConnectionDBPostgres
from scrapy_3.db.conn_mongo import ConnectionDBMongo
from scrapy_3.db.models import Competition, Kernel
import kaggle
import datetime


class Scrapy3Pipeline:

    # batch_size_competition = 2
    # batch_size_kernel = 15

    def __init__(self, *args, **kwargs):
        logging.critical("fg pipelines23 scrapy3Pipeline __init__ 10")
        super().__init__(*args, **kwargs)
        
        pass

    @classmethod
    def from_crawler(cls, crawler):
        logging.critical("fg pipelines23 scrapy3Pipeline from_crawler 20")
        try:
            pipeline = cls()
            crawler.signals.connect(pipeline.spider_opened, signal=signals.spider_opened)
            crawler.signals.connect(pipeline.spider_closed, signal=signals.spider_closed)
            crawler.signals.connect(pipeline.item_scraped, signal=signals.item_scraped)
            crawler.signals.connect(pipeline.item_dropped, signal=signals.item_dropped)
        except Exception as e:
            logging.critical(f"fg pipelines23 scrapy3Pipeline from_crawler 20 error: {e}")
        return pipeline

    def spider_opened(self, spider):
        logging.critical("fg pipelines23 scrapy3Pipeline spider_opened 30")
        
        pass
        
        
    def spider_closed(self, spider):
        logging.critical("fg pipelines23 scrapy3Pipeline spider_closed 40")
        pass
        
        
    def item_scraped(self, item, response, spider):
        logging.critical("fg pipelines23 scrapy3Pipeline item_scraped 50")     
        pass

    def item_dropped(self, item, response, spider): 
        logging.critical("fg pipelines23 scrapy3Pipeline item_dropped 60")     
        pass
    
    def process_item(self, item, spider):  
        logging.critical("fg pipelines23 scrapy3Pipeline process_item 70")   
        
        if item['pipetype'] == 'postgres':
            kernelId = item['kernelId']
            competitionId = item['competitionId']  
            tag1 = item['tag1']   
            task_id_p = item['task_id_p']   
            spider_p = item['spider_p']   
            ip_p = item['ip_p']   
            docker_id_p = item['docker_id_p']   
            worker_id_p = item['worker_id_p']   

            with self.postgres.session_scope("kaggle") as session:
                kernel = Kernel(
                    kernelId = kernelId,
                    competitionId = competitionId,
                    tag1 = tag1,
                    task_id_p = task_id_p,
                    spider_p = spider_p,
                    ip_p = ip_p,
                    docker_id_p = docker_id_p,
                    worker_id_p = worker_id_p,
                    time_p = datetime.datetime.now()
                )
                exists = session.query(Kernel).filter_by(kernelId=kernelId, competitionId=competitionId).first()
                if not exists:
                    session.add(kernel) 
                    logging.critical(f"add db kernelId={kernelId} competitionId={competitionId}")
                    session.commit()        

            return item
        
        if item['pipetype'] == 'mongo':

            detail = item['detail']
            try:                
                document = {                    
                    'detail': item.get('detail')
                }                
                self.mongo.collection.insert_one(document)
                logging.critical(f"insert mongo sucessful")
            except Exception as e:
                logging.critical(f"insert mongo error {e} ")


    def open_spider(self, spider):
        logging.critical("fg pipelines23 scrapy3Pipeline open_spider 80")                
        
        self.postgres = ConnectionDBPostgres("kaggle") 
        self.mongo = ConnectionDBMongo("kaggle", "kernels")  
        # self.get_more_date_from_postgres(spider)                             

        pass

    def close_spider(self, spider):
        logging.critical("fg pipelines23 scrapy3Pipeline close_spider 90")
        pass

    # def get_more_date_from_postgres(self, spider):
    #     logging.critical("fg pipelines23 scrapy3Pipeline get_more_date_from_postgres 100")

    #     if not hasattr(self, 'postgres') or self.postgres is None:
    #         self.postgres = ConnectionDBPostgres("kaggle")

    #     spider.pending_ids = None
    #     with self.postgres.session_scope("kaggle") as session:
    #         logging.critical(f"fenggen conn finished")
    #         query = session.query(Competition)
    #         competitions = query.filter(Competition.tag1=="0").limit(spider.batch_size_competition).all()
           
    #         for competition in competitions:                
    #             spider.pending_ids.append(competition.id)
                
    #         logging.critical(f"fenggen conn finished2")    
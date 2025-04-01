# Define your item pipelines24 here
#
# Don't forget to add your pipeline to the ITEM_pipelines12 setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
from scrapy import signals
from scrapy_3.db.conn_postgres import ConnectionDBPostgres
from scrapy_3.db.conn_mongo import ConnectionDBMongo
import datetime
from scrapy_3.db.models import Kernel 


class Scrapy3Pipeline:

    def __init__(self):
        logging.critical("fg pipelines24 scrapy3Pipeline __init__ 10")        
        pass

    @classmethod
    def from_crawler(cls, crawler):
        logging.critical("fg pipelines24 scrapy3Pipeline from_crawler 20")
        try:
            pipeline = cls()
            crawler.signals.connect(pipeline.spider_opened, signal=signals.spider_opened)
            crawler.signals.connect(pipeline.spider_closed, signal=signals.spider_closed)
            crawler.signals.connect(pipeline.item_scraped, signal=signals.item_scraped)
            crawler.signals.connect(pipeline.item_dropped, signal=signals.item_dropped)
        except Exception as e:
            logging.critical(f"fg pipelines24 scrapy3Pipeline from_crawler 20 error: {e}")
        return pipeline

    def spider_opened(self, spider):
        logging.critical("fg pipelines24 scrapy3Pipeline spider_opened 30")
        pass
        
        
    def spider_closed(self, spider):
        logging.critical("fg pipelines24 scrapy3Pipeline spider_closed 40")
        pass
        
        
    def item_scraped(self, item, response, spider):
        logging.critical("fg pipelines24 scrapy3Pipeline item_scraped 50")     
        pass

    def item_dropped(self, item, response, spider): 
        logging.critical("fg pipelines24 scrapy3Pipeline item_dropped 60")     
        pass
    
    def process_item(self, item, spider):  
        logging.critical("fg pipelines24 scrapy3Pipeline process_item 70")  
        
        kernelId = item.get('kernelId') 
        tag1 = item.get('tag1') 
        task_id_c = item.get('task_id_c')  
        spider_c = item.get('spider_c')  
        ip_c = item.get('ip_c')  
        docker_id_c = item.get('docker_id_c')  
        worker_id_c = item.get('worker_id_c')
        logging.critical("fg pipelines24 task_id_c={task_id_c}")


        if item.get('pipetype') == 'postgres':
            logging.critical(f"fenggen item kernelId={kernelId}")      
            logging.critical(f"fenggen update db tag1 successful tag1={tag1}")
            logging.critical(f"fenggen update db task_id_c successful task_id_c={task_id_c}") 
            logging.critical(f"fenggen update db spider_c successful spider_c={spider_c}") 
            logging.critical(f"fenggen update db ip_c successful ip_c={ip_c}") 
            logging.critical(f"fenggen update db docker_id_c successful docker_id_c={docker_id_c}") 
            logging.critical(f"fenggen update db worker_id_c successful worker_id_c={worker_id_c}")                      

            with self.postgres.session_scope("kaggle") as session:                
                try:
                    kernel = session.query(Kernel).filter_by(kernelId=kernelId).first()
                    if kernel:
                        kernel.tag1 = tag1
                        kernel.task_id_c = task_id_c
                        kernel.spider_c = spider_c
                        kernel.ip_c = ip_c
                        kernel.docker_id_c = docker_id_c
                        kernel.worker_id_c = worker_id_c
                        kernel.time_c = datetime.datetime.now()
                        
                        session.commit()                       
                       
                except Exception as e:
                    logging.critical(f"fenggen kernelId={kernelId} not found: {e}")     
                    session.rollback()

            return item

        if item.get('pipetype') == 'mongo':
            # logging.critical(f"fenggen item details={item.get('detail')}")
            detail = item.get('detail')
            try:
                # detail = item.get('detail')
                document = {
                    '_id': kernelId,
                    'detail': detail
                }                

                existing_doc = self.mongo.collection.find_one({                    
                    '_id': kernelId                    
                })

                if existing_doc:
                    logging.info(f"Document with ID {kernelId} exist and update it")
                    self.mongo.collection.update_one({'_id': kernelId}, {'$set': {'detail': detail}})
                else:
                    self.mongo.collection.insert_one(document)
                    logging.critical(f"insert mongo sucessful {kernelId}")

            except Exception as e:
                logging.critical(f"insert mongo error {e} ")
        

    def open_spider(self, spider):
        logging.critical("fg pipelines24 scrapy3Pipeline open_spider 80")

        # spider.pending_ids = []
        self.postgres = ConnectionDBPostgres("kaggle")
        # self.get_more_date_from_postgres(spider)        

        self.mongo = ConnectionDBMongo('kaggle', 'notebooks')  
              

        pass

    def close_spider(self, spider):
        logging.critical("fg pipelines24 scrapy3Pipeline close_spider 90")
        pass

 
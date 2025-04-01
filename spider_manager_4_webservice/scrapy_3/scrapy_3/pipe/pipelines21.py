# Define your item pipelines21 here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
from scrapy import signals
from scrapy_3.db.conn_postgres import ConnectionDBPostgres
from scrapy_3.db.conn_mongo import ConnectionDBMongo
from scrapy_3.db.models import Competition
import kaggle
import datetime


class Scrapy3Pipeline:

    def __init__(self, *args, **kwargs):
        logging.critical("fg pipelines21 scrapy3Pipeline __init__ 10")
        super().__init__(*args, **kwargs)
        
        pass

    @classmethod
    def from_crawler(cls, crawler):
        logging.critical("fg pipelines21 scrapy3Pipeline from_crawler 20")
        try:
            pipeline = cls()
            crawler.signals.connect(pipeline.spider_opened, signal=signals.spider_opened)
            crawler.signals.connect(pipeline.spider_closed, signal=signals.spider_closed)
            crawler.signals.connect(pipeline.item_scraped, signal=signals.item_scraped)
            crawler.signals.connect(pipeline.item_dropped, signal=signals.item_dropped)
        except Exception as e:
            logging.critical(f"fg pipelines21 scrapy3Pipeline from_crawler 20 error: {e}")
        return pipeline

    def spider_opened(self, spider):
        logging.critical("fg pipelines21 scrapy3Pipeline spider_opened 30")
        
        pass
        
        
    def spider_closed(self, spider):
        logging.critical("fg pipelines21 scrapy3Pipeline spider_closed 40")
        pass
        
        
    def item_scraped(self, item, response, spider):
        logging.critical("fg pipelines21 scrapy3Pipeline item_scraped 50")     
        pass

    def item_dropped(self, item, response, spider): 
        logging.critical("fg pipelines21 scrapy3Pipeline item_dropped 60")     
        pass
    
    def process_item(self, item, spider):  
        logging.critical("fg pipelines21 scrapy3Pipeline process_item 70")   
        
        if item['pipetype'] == 'postgres':
            id = item['id']
            name = item['name']        
            task_id_p = item['task_id_p']
            spider_p = item['spider_p']
            ip_p = item['ip_p']
            docker_id_p = item['docker_id_p']
            worker_id_p = item['worker_id_p']
            logging.critical(f"fenggen ---, worker_id_p={worker_id_p}")

            
            with self.postgres.session_scope("kaggle") as session:

                try:
                    competition = Competition(
                        id = id,
                        name = name,
                        task_id_p = task_id_p,
                        spider_p = spider_p,
                        ip_p = ip_p,
                        docker_id_p = docker_id_p,
                        worker_id_p = worker_id_p, 
                        time_p = datetime.datetime.now()
                    )
                    exists = session.query(Competition).filter_by(id=id).first()
                    if not exists:
                        session.add(competition) 
                        logging.critical(f"add db id={id}")
                        session.commit()        
                    else:
                        exists.tag1 = '0'
                        session.commit()
                        logging.critical(f"fenggen update db tag1 successful id={id}")
                except Exception as e:
                    logging.critical(f"fenggen postgre error={e}")     
                    session.rollback()

            return item
        
        if item['pipetype'] == 'mongo':
            detail = item['detail']

            try:
                # detail = item.get('detail')
                document = {
                    '_id': item.get('id'),
                    'detail': item.get('detail')
                }         

                existing_doc = self.mongo.collection.find_one({                    
                    '_id': item.get('id')                    
                })

                if existing_doc:
                    logging.info(f"Document with ID {item.get('id') } exist and update it")
                    self.mongo.collection.update_one({'_id': item.get('id')}, {'$set': {'detail': detail}})
                else:
                    self.mongo.collection.insert_one(document)
                    logging.critical(f"insert mongo sucessful {item.get('id')}")
                
            except Exception as e:
                logging.critical(f"insert mongo error {e} ")
                session.rollback()


    def open_spider(self, spider):
        logging.critical("fg pipelines21 scrapy3Pipeline open_spider 80")                
        
        self.postgres = ConnectionDBPostgres("kaggle") 
        self.mongo = ConnectionDBMongo("kaggle", "competitions")        

        pass

    def close_spider(self, spider):
        logging.critical("fg pipelines21 scrapy3Pipeline close_spider 90")
        pass

    
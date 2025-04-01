import scrapy
import scrapy
import logging
from scrapy import signals
import logging
from scrapy_3.items import Scrapy3ItemStackOverflow
import redis
from scrapy.utils.project import get_project_settings
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from scrapy_3.db.models import Parameters


class Web11Spider(scrapy.Spider):
    name = "web11spider"    
    allowed_domains = ["stackoverflow.com"]

    custom_settings = {
        'CONCURRENT_REQUESTS': 4,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'ITEM_PIPELINES': {
            "scrapy_3.pipe.pipelines11.Scrapy3Pipeline": 300,         
        }
    }    

    task_id_p = None
    spider_p = None
    ip_p = None
    docker_id_p = None 
    worker_id_p = None

    def __init__(self, **kwargs):
        logging.critical("fg web11 __init__ 0")

        for key, value in kwargs.items():
            logging.critical(f"key={key} value={value}")
            if key == 'task_id':
                self.task_id_p = value
            if key == 'spider':
                self.spider_p = value
            if key == 'ip':
                self.ip_p = value
            if key == 'docker_id':
                self.docker_id_p = value
            if key == 'worker_id':
                self.worker_id_p = value
                

        # self.settings = get_project_settings()

        # logging.critical(f"fenggen --page={self.page}")
        params = self.load_params_from_db()
        for key, value in params.items():
            setattr(self, key, value) 
        logging.critical(f"fenggen --page={self.page}")       

        try:
            self.redis_conn = redis.Redis(
                host = self.REDIS_HOST,
                port = self.REDIS_PORT,
            )
        except Exception as e:
            logging.critical(f"fenggen redis conn error {e}")
        
        logging.critical("redis conn sucessful")

        # logging.critical(f"fenggen redis_host={redis_host}, redis_port={redis_port}")
        pass


    def load_params_from_db(self):
        # 数据库读取逻辑，类似前面的例子
            
        try:                
            engine_questionshunt = create_engine('postgresql://postgres:Fg285426*@192.168.0.58:5432/questionshunt')            
            with engine_questionshunt.connect() as conn:
                pass

        except Exception as e:
            logging.critical(f"fenggen engine_questionshunt.connect error {e}")        
            
        session_questionshunt = sessionmaker(bind=engine_questionshunt)()

        params_query = session_questionshunt.query(Parameters).filter_by(crawler_name=self.name).all()

        params_dict = {}

        for param in params_query:
            # 根据参数类型进行转换
            if param.parameter_type == 'integer':
                value = int(param.parameter_value)
            elif param.parameter_type == 'float':
                value = float(param.parameter_value)
            elif param.parameter_type == 'boolean':
                value = param.parameter_value.lower() == 'true'
            elif param.parameter_type == 'json':
                value = json.loads(param.parameter_value)
            else:
                value = param.parameter_value

            params_dict[param.parameter_key] = value
            logging.critical(f"key={param.parameter_key} val={value}")

        logging.critical(f"reading sucessful [web11spider]  {len(params_dict)} ")
        return params_dict    

 

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        logging.critical("fg web11 from_crawler 5")
        spider = super(Web11Spider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.engine_started, signal=signals.engine_started)
        crawler.signals.connect(spider.engine_stopped, signal=signals.engine_stopped)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.spider_error, signal=signals.spider_error)
        crawler.signals.connect(spider.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(spider.request_dropped, signal=signals.request_dropped)
        crawler.signals.connect(spider.request_reached_downloader, signal=signals.request_reached_downloader)
        crawler.signals.connect(spider.response_received, signal=signals.response_received)
        crawler.signals.connect(spider.response_downloaded, signal=signals.response_downloaded)
        crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(spider.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(spider.item_error, signal=signals.item_error)
        crawler.signals.connect(spider.stats_spider_opened, signal=signals.stats_spider_opened)
        crawler.signals.connect(spider.stats_spider_closing, signal=signals.stats_spider_closing)
        crawler.signals.connect(spider.stats_spider_closed, signal=signals.stats_spider_closed)
        crawler.signals.connect(spider.headers_received, signal=signals.headers_received)
        crawler.signals.connect(spider.bytes_received, signal=signals.bytes_received)
        # crawler.signals.connect(spider.offsite_request_dropped, signal=signals.offsite_request_dropped)
        # crawler.signals.connect(spider.update_telnet_vars, signal=signals.update_telnet_vars)
        # crawler.signals.connect(spider.capture_file_opened, signal=signals.capture_file_opened)
        # crawler.signals.connect(spider.capture_file_closed, signal=signals.capture_file_closed)

        return spider

    def engine_started(self):
        logging.critical("fg web11 engine_started 10")
        pass

    def engine_stopped(self):
        logging.critical("fg web11 engine_stopped 20")
        pass

    def spider_opened(self, spider):
        logging.critical("fg web11 spider_opened 30")
        pass

    def spider_idle(self, spider):
        logging.critical("fg web11 spider_idle 40")
        pass

    def spider_closed(self, spider):
        logging.critical("fg web11 spider_closed 50")
        pass
    

    def spider_error(self, spider):
        logging.critical("fg web11 spider_error 60")
        pass

    def request_scheduled(self, spider):
        logging.critical("fg web11 request_scheduled 70")
        pass

    def request_dropped(self, spider):
        logging.critical("fg web11 request_dropped 80")
        pass

    def request_reached_downloader(self, spider):
        logging.critical("fg web11 request_reached_downloader 90")
        pass

    def response_received(self, spider):
        logging.critical("fg web11 response_received 100")
        pass
    

    def response_downloaded(self, spider):
        logging.critical("fg web11 response_downloaded 110")
        pass

    def item_scraped(self, spider):
        logging.critical("fg web11 item_scraped 120")
        pass

    def item_dropped(self, spider):
        logging.critical("fg web11 item_dropped 130")
        pass

    def item_error(self, spider):
        logging.critical("fg web11 item_error 140")
        pass

    def stats_spider_opened(self, spider):
        logging.critical("fg web11 stats_spider_opened 150")
        pass


    def stats_spider_closing(self, spider):
        logging.critical("fg web11 stats_spider_closing 160")
        pass

    def stats_spider_closed(self, spider):
        logging.critical("fg web11 stats_spider_closed 170")
        pass

    def headers_received(self, spider):
        logging.critical("fg web11 headers_received 180")
        pass

    def bytes_received(self, spider):
        logging.critical("fg web11 bytes_received 190")
        pass

    def offsite_request_dropped(self, spider):
        logging.critical("fg web11 offsite_request_dropped 200")
        pass


    def update_telnet_vars(self, spider):
        logging.critical("fg web11 update_telnet_vars 210")
        pass

    def capture_file_opened(self, spider):
        logging.critical("fg web11 capture_file_opened 220")
        pass

    def capture_file_closed(self, spider):
        logging.critical("fg web11 capture_file_closed 230")
        pass                  

    def start_requests(self):
        logging.critical("fg web11 start_requests 240")
        url = self.url_main        
        logging.critical(f"fenggen11 url={url}")
        yield scrapy.Request(
            url = url,
            callback = self.parse
        )

    def parse(self, response):
        
        logging.critical("fg web11 parse 250")

        logging.critical(f"fenggen response.status={response.status}")
        if response.status != 200:
            return                
        
        questions = response.xpath(self.XPATH_1).getall() 
        
        for question in questions:
            logging.critical(f"fenggen questions={questions}")            
            title = question.split("/")[-1]
            question_id = question.split("/")[-2]            

            self.redis_conn.lpush("detail_url_queue", json.dumps(
                {
                    'detail_url': f"{self.domain_url}{question}",
                    'question_id': question_id,
                    'title': title,
                    'taskid': self.task_id_p               
                }
            ))
            logging.critical(f"fenggen redisqueue url={self.domain_url}{question}, question_id={question_id}, title={title}")
            logging.critical(f"fenggen web11 taskid={self.task_id_p} spider_p={self.spider_p} ip_p={self.ip_p} docker_id_p={self.docker_id_p}")
            
            item = Scrapy3ItemStackOverflow()
            item['question_id'] = question_id
            item['title'] = title     
            item['task_id_p'] = self.task_id_p
            item['spider_p'] = self.spider_p
            item['ip_p'] = self.ip_p
            item['docker_id_p'] = self.docker_id_p 
            item['worker_id_p'] = self.worker_id_p   
            logging.critical(f"fenggen --web11 worker_id_p={self.worker_id_p} ip_p={self.ip_p} docker_id_p={self.docker_id_p}")
            yield item      
        
        
        self.page += 1
        url = f'{self.url_main}&page={self.page}'
        logging.critical(f"fenggen url={url}")
        yield scrapy.Request(
            url = url,
            callback = self.parse
        ) 
        
            
        

        




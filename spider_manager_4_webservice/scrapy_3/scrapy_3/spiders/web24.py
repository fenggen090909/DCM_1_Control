import scrapy
import scrapy
import logging
from scrapy import signals
import logging
from scrapy_3.items import Scrapy3Item_Kaggle_Kernel
from scrapy_3.pipe.pipelines12 import Scrapy3Pipeline
import redis
from scrapy.utils.project import get_project_settings
import json 
import signal
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from scrapy_3.db.models import Parameters
import sys


class Web24Spider(scrapy.Spider):
    name = "web24spider"    
    allowed_domains = ["kaggle.com"]

    custom_settings = {
        'CONCURRENT_REQUESTS': 16,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
        'ITEM_PIPELINES': {            
            "scrapy_3.pipe.pipelines24.Scrapy3Pipeline": 300,            
        }
    }

    task_id_c = None
    spider_c = None
    ip_c = None
    docker_id_c = None 
    worker_id_c = None

    def __init__(self, **kwargs):
        logging.critical("fg web24 __init__ 0")
        self.logger.critical("fg web24 __init__ 0 - using self.logger")
        print("fg web24 __init__ 0 - using print")

        for key, value in kwargs.items():
            logging.critical(f"key={key} value={value}")
            if key == 'task_id':
                self.task_id_c = value
            if key == 'spider':
                self.spider_c = value
            if key == 'ip':
                self.ip_c = value
            if key == 'docker_id':
                self.docker_id_c = value
            if key == 'worker_id':
                self.worker_id_c = value

        # settings = get_project_settings()
        params = self.load_params_from_db()
        for key, value in params.items():
            setattr(self, key, value) 
            logging.critical(f"fenggen --self.{key}={value}") 

        # logging.critical(f"fenggen --self.kernelId={self.kernelId}")  

        try:
            self.redis_conn = redis.Redis(
                host = self.REDIS_HOST,
                port = self.REDIS_PORT,
            )
        except Exception as e:
            logging.critical(f"fenggen redis conn error {e}")
        
        logging.critical("redis conn sucessful")                

        pass

    def load_params_from_db(self):
            # 数据库读取逻辑，类似前面的例子
                
            try:                
                engine_kaggle = create_engine('postgresql://postgres:Fg285426*@192.168.0.58:5432/kaggle')            
                with engine_kaggle.connect() as conn:
                    pass

            except Exception as e:
                logging.critical(f"fenggen engine_kaggle.connect error {e}")        
                
            session_kaggle = sessionmaker(bind=engine_kaggle)()

            params_query = session_kaggle.query(Parameters).filter_by(crawler_name=self.name).all()

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

            logging.critical(f"reading sucessful [web24spider]  {len(params_dict)} ")
            return params_dict 

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        logging.critical("fg web24 from_crawler 5")
        spider = super(Web24Spider, cls).from_crawler(crawler, *args, **kwargs)
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

        # crawler.signals.connect(spider.signal_handler, signal=signal.SIGINT)
        
        # crawler.signals.connect(spider.offsite_request_dropped, signal=signals.offsite_request_dropped)
        # crawler.signals.connect(spider.update_telnet_vars, signal=signals.update_telnet_vars)
        # crawler.signals.connect(spider.capture_file_opened, signal=signals.capture_file_opened)
        # crawler.signals.connect(spider.capture_file_closed, signal=signals.capture_file_closed)

        return spider

    def engine_started(self):
        logging.critical("fg web24 engine_started 10")
        pass

    def engine_stopped(self):
        logging.critical("fg web24 engine_stopped 20")
        pass

    def spider_opened(self, spider):
        logging.critical("fg web24 spider_opened 30")
        pass

    def spider_idle(self, spider):
        logging.critical("fg web24 spider_idle 40")
        pass

    def spider_closed(self, spider):
        logging.critical("fg web24 spider_closed 50")
        pass
    

    def spider_error(self, spider):
        logging.critical("fg web24 spider_error 60")
        pass

    def request_scheduled(self, spider):
        logging.critical("fg web24 request_scheduled 70")
        pass

    def request_dropped(self, spider):
        logging.critical("fg web24 request_dropped 80")
        pass

    def request_reached_downloader(self, spider):
        logging.critical("fg web24 request_reached_downloader 90")
        pass

    def response_received(self, spider):
        logging.critical("fg web24 response_received 100")
        pass
    

    def response_downloaded(self, spider):
        logging.critical("fg web24 response_downloaded 110")
        pass

    def item_scraped(self, item, response, spider):
        logging.critical("fg web24 item_scraped 120")        
        pass

    def item_dropped(self, spider):
        logging.critical("fg web24 item_dropped 130")
        pass

    def item_error(self, spider):
        logging.critical("fg web24 item_error 140")
        pass

    def stats_spider_opened(self, spider):
        logging.critical("fg web24 stats_spider_opened 150")
        pass


    def stats_spider_closing(self, spider):
        logging.critical("fg web24 stats_spider_closing 160")
        pass

    def stats_spider_closed(self, spider):
        logging.critical("fg web24 stats_spider_closed 170")
        pass

    def headers_received(self, spider):
        logging.critical("fg web24 headers_received 180")
        pass

    def bytes_received(self, spider):
        logging.critical("fg web24 bytes_received 190")
        pass

    def offsite_request_dropped(self, spider):
        logging.critical("fg web24 offsite_request_dropped 200")
        pass


    def update_telnet_vars(self, spider):
        logging.critical("fg web24 update_telnet_vars 210")
        pass

    def capture_file_opened(self, spider): 
        logging.critical("fg web24 capture_file_opened 220")
        pass

    def capture_file_closed(self, spider):
        logging.critical("fg web24 capture_file_closed 230")
        pass   

    # def signal_handler(sig, frame):
    #     print('You pressed Ctrl+C!')
    #     # 在这里添加清理代码，例如关闭数据库连接、保存数据等
    #     self.redis_client.close()
    #     sys.exit(0)

    # signal.signal(signal.SIGINT, signal_handler)                   

    def start_requests(self):
        logging.critical("fg web24 start_requests 240")  
        # sys.stdout.flush()
        # sys.stderr.flush()
        
        # 获取第一个任务启动爬虫
        task = self.redis_conn.brpop('kaggle_notebook_queue', timeout=5)

        if task:
            # 注意这里使用yield
            yield self._process_task(task)
        else:
            # 如果没有任务，也要返回一个初始请求来检查队列
            logging.critical("Initial queue is empty, will check again...")
            yield scrapy.Request(
                url=self.url_virtual,  # 虚拟URL
                callback=self.check_queue,
                dont_filter=True
            )               


    # {"kernelId": 79398632, "competitionId": "91496", "scriptUrl": "/code/drabdulbasetaledresi/notebooke15d3bce37"}
    def _process_task(self, task):
        _, data_raw = task
        data = json.loads(data_raw)
        logging.critical(f"fenggen redis data={data}")
        self.kernelId = data['kernelId']
        self.competitionId = data['competitionId']
        self.scriptUrl = data['scriptUrl']
        
        logging.critical(f"fenggen redis kernelId={self.kernelId} competitionId={self.competitionId} scriptUrl={self.scriptUrl}")
        # sys.stdout.flush()
        # sys.stderr.flush()
        
        # 返回一个请求对象，而不是直接yield
        return scrapy.Request(
            url=f"{self.url_main}{self.scriptUrl}",
            callback=self.parse,
            errback=self.error_handler,
            dont_filter=True
        )

    def parse(self, response):
        # 处理当前任务
        logging.critical(f"fg parse called for {response.url}")
        sys.stdout.flush()
        sys.stderr.flush()

        if response.status != 200:
            return

        # content = response.xpath(self.XPATH_1).get()        
        # logging.critical(f"fenggen url={response.url} question_id={self.question_id} content={content}")
        content = response.body.decode('utf-8')
        logging.critical(f"fenggen response={content}")

        item_postgres = Scrapy3Item_Kaggle_Kernel()
        item_postgres['kernelId'] = self.kernelId
        item_postgres['tag1'] = '1'            
        item_postgres['task_id_c'] = self.task_id_c
        item_postgres['spider_c'] = self.spider_c
        item_postgres['ip_c'] = self.ip_c
        item_postgres['docker_id_c'] = self.docker_id_c
        item_postgres['worker_id_c'] = self.worker_id_c
        item_postgres['pipetype'] = 'postgres'
        yield item_postgres

        item_mongo = Scrapy3Item_Kaggle_Kernel()
        item_mongo['detail'] = content
        item_mongo['kernelId'] = self.kernelId
        item_mongo['pipetype'] = 'mongo'
        yield item_mongo
        
        # 处理完当前任务后，尝试获取下一个任务
        task = self.redis_conn.brpop('kaggle_notebook_queue', timeout=5)
        if task:
            yield self._process_task(task)
        else:
            logging.critical("No more tasks, waiting...")
            # 可选：设置一个新请求来再次检查队列
            yield scrapy.Request(
                url=self.url_virtual,  # 虚拟URL
                callback=self.check_queue,
                dont_filter=True,
                priority=-100,  # 低优先级
                meta={"wait": True}
            )

    def check_queue(self, response):
        # 再次检查队列
        task = self.redis_conn.brpop('kaggle_notebook_queue', timeout=5)
        if task:
            yield self._process_task(task)
        else:
            # 如果仍然没有任务，可以再次调度检查
            yield scrapy.Request(
                url=self.url_virtual,
                callback=self.check_queue,
                dont_filter=True,
                priority=-100,
                meta={"wait": True}
            )    

    def error_handler(self, failure):
        # 处理请求错误
        logging.critical(f"Request failed: {failure}")
        sys.stdout.flush()
        sys.stderr.flush()
        # 尝试获取下一个任务
        task = self.redis_conn.brpop('kaggle_notebook_queue', timeout=5)
        if task:
            yield self._process_task(task)
        

        






        

            
        

        




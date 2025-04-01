import scrapy
import scrapy
import logging
from scrapy import signals
import logging
import kaggle
from scrapy_3.items import Scrapy3Item_Kaggle_Kernel
import json
import redis
from scrapy.exceptions import CloseSpider
from scrapy_3.db.models import Parameters
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Web23Spider(scrapy.Spider):
    name = "web23spider"
    allowed_domains = ["kaggle.com"] 

    # page = 1
    # kernel_count = 0
    # batch_size_competition = 2
    # batch_size_kernel = 10
    param_competitionId = None    

    # url_main = "https://www.kaggle.com/api/v1/"
    # url_main = "https://www.kaggle.com"
    # url_api = "https://www.kaggle.com/api/i/kernels.KernelsService/ListKernels"

    custom_settings = {
        'CONCURRENT_REQUESTS': 4,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'ITEM_PIPELINES': {
            "scrapy_3.pipe.pipelines23.Scrapy3Pipeline": 300,            
        }
    }

    def __init__(self, competitionId=None, *args, **kwargs):

        logging.critical("fg web23 __init__ 0")
        super().__init__(*args, **kwargs)          

        if competitionId == None:
            logging.critical("fg web23 CloseSpider")
            raise CloseSpider('no competitionId')            
        else:
            self.param_competitionId = competitionId

        for key, value in kwargs.items():
            logging.critical(f"key={key} value={value}")
            if key == 'task_id':
                self.task_id_p = value
                logging.critical(f"self.task_id_p={self.task_id_p}")
            if key == 'spider':
                self.spider_p = value
                logging.critical(f"self.spider_p{self.spider_p}")
            if key == 'ip':
                self.ip_p = value
                logging.critical(f"self.ip_p={self.ip_p}")
            if key == 'docker_id':
                self.docker_id_p = value
                logging.critical(f"self.docker_id_p={self.docker_id_p}")
            if key == 'worker_id':
                self.worker_id_p = value
                logging.critical(f"self.worker_id_p={self.worker_id_p}")

        params = self.load_params_from_db()
        for key, value in params.items():
            setattr(self, key, value) 
            logging.critical(f"fenggen web23spider self.{key}={value}") 

        try:
            self.redis_conn = redis.Redis(
                host = self.REDIS_HOST,
                port = self.REDIS_PORT,
            )
        except Exception as e:
            logging.critical(f"fenggen redis conn error {e}")
        
        logging.critical("redis conn sucessful")

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

        logging.critical(f"reading sucessful [web21spider]  {len(params_dict)} ")
        return params_dict 

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        logging.critical("fg web23 from_crawler 5")
        spider = super(Web23Spider, cls).from_crawler(crawler, *args, **kwargs)
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
        logging.critical("fg web23 engine_started 10")
        pass

    def engine_stopped(self):
        logging.critical("fg web23 engine_stopped 20")
        pass

    def spider_opened(self, spider):
        logging.critical("fg web23 spider_opened 30")
        pass

    def spider_idle(self, spider):
        logging.critical("fg web23 spider_idle 40")
        pass
        
        

    def spider_closed(self, spider):
        logging.critical("fg web23 spider_closed 50")
        pass
    

    def spider_error(self, spider):
        logging.critical("fg web23 spider_error 60")
        pass

    def request_scheduled(self, spider):
        logging.critical("fg web23 request_scheduled 70")
        pass

    def request_dropped(self, spider):
        logging.critical("fg web23 request_dropped 80")
        pass

    def request_reached_downloader(self, spider):
        logging.critical("fg web23 request_reached_downloader 90")
        pass

    def response_received(self, spider):
        logging.critical("fg web23 response_received 100")
        pass
    

    def response_downloaded(self, spider):
        logging.critical("fg web23 response_downloaded 110")
        pass

    def item_scraped(self, item, response, spider):
        logging.critical("fg web23 item_scraped 120")   
        logging.critical(f"Item scraped: {item}") 

        self.kernel_count += 0.5
        logging.critical(f"fenggen kernel_count={self.kernel_count}")
        if self.kernel_count % self.batch_size_kernel == 0:
            logging.critical("fenggen web12 item_scraped start getting next batch")            
            self.page += 1
            request = self.create_next_page_request()
            if isinstance(request, scrapy.Request):
                logging.critical("Request object is valid, scheduling it")
                self.crawler.engine.crawl(request)
            else:
                logging.critical(f"Invalid request object type: {type(request)}")


    def create_next_page_request(self):                                  
        logging.critical("fg web23 create_next_page_request 125")
        payload = {                                                            
            "kernelFilterCriteria": {
                "search": "",
                "listRequest": {
                    "competitionId": self.param_competitionId,
                    "sortBy": "HOTNESS",
                    "pageSize": self.batch_size_kernel,
                    "group": "EVERYONE",
                    "page": self.page,
                    "modelIds": [],
                    "modelInstanceIds": [],
                    "excludeKernelIds": [],
                    "tagIds": "",
                    "excludeResultsFilesOutputs": False,
                    "wantOutputFiles": False,
                    "excludeNonAccessedDatasources": True
                }
            },
            "detailFilterCriteria": {
                "deletedAccessBehavior": "RETURN_NOTHING",
                "unauthorizedAccessBehavior": "RETURN_NOTHING",
                "excludeResultsFilesOutputs": False,
                "wantOutputFiles": False,
                "kernelIds": [],
                "outputFileTypes": [],
                "includeInvalidDataSources": False
            },
            "readMask": "pinnedKernels"            
        }
        headers = {
            'Content-Type': 'application/json',            
            'accept': 'application/json',                       
            'X-XSRF-TOKEN': self.xsrf_token,
            'accept-encoding':'gzip, deflate, br, zstd',
            'accept-language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cache-control':'no-cache',   
            'origin': 'https://www.kaggle.com',
            'pragma':'no-cache',
            'priority':'u=1, i',
            # 'referer':'https://www.kaggle.com/datasets',
            # 'sec-ch-ua':'"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            # 'sec-ch-ua-mobile':'?0',
            # 'sec-ch-ua-platform':"Windows",
            # 'sec-fetch-dest':'empty',
            # 'sec-fetch-mode':'cors',
            # 'sec-fetch-site':'same-origin',
            # 'x-kaggle-build-version':'f0fbb334ca7a09441642a5253344731ceb2546bb',
        }

        logging.critical("fenggen start1 request()")

        return scrapy.Request(
            url=self.url_api,
            method='POST',
            body=json.dumps(payload),
            headers=headers,
            cookies=self.cookies,
            callback=self.parse,       
    )
        # self.crawler.engine.crawl(request)   
        # yield request                                 

    def item_dropped(self, spider):
        logging.critical("fg web23 item_dropped 130")
        pass

    def item_error(self, spider):
        logging.critical("fg web23 item_error 140")
        pass

    def stats_spider_opened(self, spider):
        logging.critical("fg web23 stats_spider_opened 150")
        pass


    def stats_spider_closing(self, spider):
        logging.critical("fg web23 stats_spider_closing 160")
        pass

    def stats_spider_closed(self, spider):
        logging.critical("fg web23 stats_spider_closed 170")
        pass

    def headers_received(self, spider):
        logging.critical("fg web23 headers_received 180")
        pass

    def bytes_received(self, spider):
        logging.critical("fg web23 bytes_received 190")
        pass

    def offsite_request_dropped(self, spider):
        logging.critical("fg web23 offsite_request_dropped 200")
        pass


    def update_telnet_vars(self, spider):
        logging.critical("fg web23 update_telnet_vars 210")
        pass

    def capture_file_opened(self, spider):
        logging.critical("fg web23 capture_file_opened 220")
        pass

    def capture_file_closed(self, spider):
        logging.critical("fg web23 capture_file_closed 230")
        pass                  

    def start_requests(self):
        logging.critical("fg web23 start_requests 240")                

        yield scrapy.Request(
            url=self.url_main,
            callback=self.get_cookies,            
        )            
        

    def get_cookies(self, response):
        logging.critical("fg web23 get_cookies 245")

        self.cookies = {}        
        for cookie in response.headers.getlist('Set-Cookie'):
            name_value = cookie.decode('utf-8').split(';')[0].split('=')
            self.cookies[name_value[0]] = name_value[1]

        self.xsrf_token = response.css('meta[name="csrf-token"]::attr(content)').get() or self.cookies.get('XSRF-TOKEN')
        if not self.xsrf_token:
            logging.critical("XSRF-TOKEN not found, request may fail")

        # self.logger.critical(f"Cookies fetched: {self.cookies}")
        # self.logger.critical(f"XSRF-TOKEN: {self.xsrf_token}")        
        
        logging.critical(f"fg fenggen competitionId={self.param_competitionId}")

        payload = {

            "kernelFilterCriteria": {
                "search": "",
                "listRequest": {
                    "competitionId": self.param_competitionId,
                    "sortBy": "HOTNESS",
                    "pageSize": self.batch_size_kernel,
                    "group": "EVERYONE",
                    "page": self.page,
                    "modelIds": [],
                    "modelInstanceIds": [],
                    "excludeKernelIds": [],
                    "tagIds": "",
                    "excludeResultsFilesOutputs": False,
                    "wantOutputFiles": False,
                    "excludeNonAccessedDatasources": True
                }
            },
            "detailFilterCriteria": {
                "deletedAccessBehavior": "RETURN_NOTHING",
                "unauthorizedAccessBehavior": "RETURN_NOTHING",
                "excludeResultsFilesOutputs": False,
                "wantOutputFiles": False,
                "kernelIds": [],
                "outputFileTypes": [],
                "includeInvalidDataSources": False
            },
            "readMask": "pinnedKernels"
                      
        }
        headers = {
            'Content-Type': 'application/json',            
            'accept': 'application/json',                       
            'X-XSRF-TOKEN': self.xsrf_token,
            'accept-encoding':'gzip, deflate, br, zstd',
            'accept-language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cache-control':'no-cache',   
            'origin': 'https://www.kaggle.com',
            'pragma':'no-cache',
            'priority':'u=1, i', 
            # 'cookie': self.cookies,
        }
        logging.critical("fenggen start request()")
        yield scrapy.Request(
            url=self.url_api,
            method='POST',
            body=json.dumps(payload),
            headers=headers,
            cookies=self.cookies,            
            callback=self.parse,        
        )

    

    def parse(self, response):
        logging.critical("fg web23 parse 250")        
        logging.critical(f"fenggen parse url={response.url} status={response.status}")        

        data = response.json()
        logging.critical(f"fenggen parse data={data}")
        logging.critical(f"fenggen parse data[kernels]={data['kernels']}")

        for kernel in data['kernels']:
            # logging.critical(f"fenggen competitionId={response.meta.get('competitionId')} kernel={kernel}")
            kernelId = kernel['id']            
            competitionId = self.param_competitionId 
            scriptUrl = kernel['scriptUrl']             

            logging.critical(f"fenggen parse_id={kernelId} competitionId={competitionId}")
            detail = kernel 

            self.redis_conn.lpush("kaggle_notebook_queue", json.dumps(
                {
                    'kernelId': kernelId,
                    'competitionId': competitionId,
                    'scriptUrl': scriptUrl                              
                }
            ))     

            item_postgres = Scrapy3Item_Kaggle_Kernel()
            item_postgres['kernelId'] = kernelId
            item_postgres['competitionId'] = competitionId
            item_postgres['tag1'] = "0"
            item_postgres['task_id_p'] = self.task_id_p
            item_postgres['spider_p'] = self.spider_p
            item_postgres['ip_p'] = self.ip_p
            item_postgres['docker_id_p'] = self.docker_id_p 
            item_postgres['worker_id_p'] = self.worker_id_p   
            logging.critical(f"fenggen --web11 worker_id_p={self.worker_id_p} ip_p={self.ip_p} docker_id_p={self.docker_id_p}")

            item_postgres['pipetype'] = 'postgres'
            
            yield item_postgres  

            item_mongo = Scrapy3Item_Kaggle_Kernel()            
            item_mongo['detail'] = detail            
            item_mongo['pipetype'] = 'mongo'
            logging.critical(f"fenggen web23 detail={detail}")            
            yield item_mongo                                     
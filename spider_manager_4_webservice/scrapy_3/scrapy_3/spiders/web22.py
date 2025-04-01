import scrapy
import scrapy
import logging
from scrapy import signals
import logging
import kaggle
from scrapy_3.items import Scrapy3Item_Kaggle_Dataset
import json
from scrapy_3.db.models import Parameters
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class web22Spider(scrapy.Spider):
    name = "web22spider"
    allowed_domains = ["kaggle.com"]    

    custom_settings = {
        'CONCURRENT_REQUESTS': 4,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'ITEM_PIPELINES': {
            "scrapy_3.pipe.pipelines22.Scrapy3Pipeline": 300,            
        }
    }

    def __init__(self, *args, **kwargs):
        self.logger.critical("fg web22 __init__ 0")
        super().__init__(*args, **kwargs)        
        
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

        params = self.load_params_from_db()
        for key, value in params.items():
            setattr(self, key, value) 
            logging.critical(f"fenggen web22spider self.{key}={value}") 

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
        logging.critical("fg web22 from_crawler 5")
        spider = super(web22Spider, cls).from_crawler(crawler, *args, **kwargs)
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
        logging.critical("fg web22 engine_started 10")
        pass

    def engine_stopped(self):
        logging.critical("fg web22 engine_stopped 20")
        pass

    def spider_opened(self, spider):
        logging.critical("fg web22 spider_opened 30")
        pass

    def spider_idle(self, spider):
        logging.critical("fg web22 spider_idle 40")
        pass

    def spider_closed(self, spider):
        logging.critical("fg web22 spider_closed 50")
        pass
    

    def spider_error(self, spider):
        logging.critical("fg web22 spider_error 60")
        pass

    def request_scheduled(self, spider):
        logging.critical("fg web22 request_scheduled 70")
        pass

    def request_dropped(self, spider):
        logging.critical("fg web22 request_dropped 80")
        pass

    def request_reached_downloader(self, spider):
        logging.critical("fg web22 request_reached_downloader 90")
        pass

    def response_received(self, spider):
        logging.critical("fg web22 response_received 100")
        pass
    

    def response_downloaded(self, spider):
        logging.critical("fg web22 response_downloaded 110")
        pass

    def item_scraped(self, spider):
        logging.critical("fg web22 item_scraped 120")        
        pass

    def item_dropped(self, spider):
        logging.critical("fg web22 item_dropped 130")
        pass

    def item_error(self, spider):
        logging.critical("fg web22 item_error 140")
        pass

    def stats_spider_opened(self, spider):
        logging.critical("fg web22 stats_spider_opened 150")
        pass


    def stats_spider_closing(self, spider):
        logging.critical("fg web22 stats_spider_closing 160")
        pass

    def stats_spider_closed(self, spider):
        logging.critical("fg web22 stats_spider_closed 170")
        pass

    def headers_received(self, spider):
        logging.critical("fg web22 headers_received 180")
        pass

    def bytes_received(self, spider):
        logging.critical("fg web22 bytes_received 190")
        pass

    def offsite_request_dropped(self, spider):
        logging.critical("fg web22 offsite_request_dropped 200")
        pass


    def update_telnet_vars(self, spider):
        logging.critical("fg web22 update_telnet_vars 210")
        pass

    def capture_file_opened(self, spider):
        logging.critical("fg web22 capture_file_opened 220")
        pass

    def capture_file_closed(self, spider):
        logging.critical("fg web22 capture_file_closed 230")
        pass                  

    def start_requests(self):
        logging.critical("fg web22 start_requests 240")                

        yield scrapy.Request(
            url=self.url_main,
            callback=self.get_cookies,            
        )            
        

    def get_cookies(self, response):
        logging.critical("fg web22 get_cookies 245")
        self.cookies = {}
        for cookie in response.headers.getlist('Set-Cookie'):
            name_value = cookie.decode('utf-8').split(';')[0].split('=')
            self.cookies[name_value[0]] = name_value[1]

        self.xsrf_token = response.css('meta[name="csrf-token"]::attr(content)').get() or self.cookies.get('XSRF-TOKEN')
        if not self.xsrf_token:
            logging.critical("XSRF-TOKEN not found, request may fail")

        # self.logger.critical(f"Cookies fetched: {cookies}")
        # self.logger.critical(f"XSRF-TOKEN: {xsrf_token}")

        
        payload = {                                                
            "page": self.page,
            "group": "DATASET_SELECTION_GROUP_PUBLIC",
            "size": "DATASET_SIZE_GROUP_ALL",
            "fileType": "DATASET_FILE_TYPE_GROUP_ALL",
            "license": "DATASET_LICENSE_GROUP_ALL",
            "viewed": "DATASET_VIEWED_GROUP_UNSPECIFIED",
            "categoryIds": [],
            "search": "",
            "sortBy": "DATASET_SORT_BY_HOTTEST",
            "includeTopicalDatasets": False,
            "minUsabilityRating": 0,
            "feedbackIds": []
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
            'referer':'https://www.kaggle.com/datasets',
            'sec-ch-ua':'"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':"Windows",
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'x-kaggle-build-version':'f0fbb334ca7a09441642a5253344731ceb2546bb',
        }
        logging.critical("fenggen start request()")
        yield scrapy.Request(
            url=self.url_api,
            method='POST',
            body=json.dumps(payload),
            headers=headers,
            cookies=self.cookies,
            callback=self.parse,
            # meta={'proxy': self.proxy, 'cookies': cookies, 'page': page}  # 添加代理
        )


    def parse(self, response):
        logging.critical("fg web22 parse 250")
        # url = str(response.url)
        logging.critical(f"fenggen parse url={response.url} status={response.status}")        

        data = response.json()
        # logging.critical(f"fenggen parse data={data}")
        for dataset in data['datasetList']['items']:
            logging.critical(f"fenggen datasetUrl={dataset['datasetUrl']}")

            id = dataset['datasource']['datasetId']
            url = dataset['datasetUrl']
            detail = dataset
            # logging.critical(f"fenggen dataset id={id} url={url}")
            # logging.critical(f"fenggen dataset detail={detail}")


            item_postgres = Scrapy3Item_Kaggle_Dataset()
            item_postgres['id'] = id
            item_postgres['url'] = url
            item_postgres['tag1'] = '0' 
            item_postgres['task_id_p'] = self.task_id_p
            item_postgres['spider_p'] = self.spider_p
            item_postgres['ip_p'] = self.ip_p
            item_postgres['docker_id_p'] = self.docker_id_p 
            item_postgres['worker_id_p'] = self.worker_id_p   
            logging.critical(f"fenggen --web11 worker_id_p={self.worker_id_p} ip_p={self.ip_p} docker_id_p={self.docker_id_p}")

            item_postgres['pipetype'] = 'postgres'
            logging.critical(f"fenggen web22 id={id}")
            logging.critical(f"fenggen web22 url={url}")
            yield item_postgres  

            item_mongo = Scrapy3Item_Kaggle_Dataset()
            item_mongo['id'] = id
            item_mongo['detail'] = detail            
            item_mongo['pipetype'] = 'mongo'
            logging.critical(f"fenggen web22 detail={detail}")            
            yield item_mongo        
        
        self.page += 1
        logging.critical(f"fenggen web22 page={self.page}")

        payload = {                                                
            "page": self.page,
            "group": "DATASET_SELECTION_GROUP_PUBLIC",
            "size": "DATASET_SIZE_GROUP_ALL",
            "fileType": "DATASET_FILE_TYPE_GROUP_ALL",
            "license": "DATASET_LICENSE_GROUP_ALL",
            "viewed": "DATASET_VIEWED_GROUP_UNSPECIFIED",
            "categoryIds": [],
            "search": "",
            "sortBy": "DATASET_SORT_BY_HOTTEST",
            "includeTopicalDatasets": False,
            "minUsabilityRating": 0,
            "feedbackIds": []
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
            'referer':'https://www.kaggle.com/datasets',
            'sec-ch-ua':'"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':"Windows",
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'x-kaggle-build-version':'f0fbb334ca7a09441642a5253344731ceb2546bb',
        }
        logging.critical("fenggen start1 request()")
        yield scrapy.Request(
            url=self.url_api,
            method='POST',
            body=json.dumps(payload),
            headers=headers,
            cookies=self.cookies,
            callback=self.parse,
            # meta={'proxy': self.proxy, 'cookies': cookies, 'page': page}  # 添加代理
        )



                                     


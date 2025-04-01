# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import logging
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from scrapy_3.db.models import Parameters


class Scrapy3ProxyMiddleware:

    def __init__(self):
        logging.critical("fg middlewares Scrapy3ProxyMiddleware __init__ 85")
        pass

    @classmethod
    def from_crawler(cls, crawler):
        logging.critical("fg middlewares Scrapy3ProxyMiddleware from_crawler 90")
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        logging.critical("fg middlewares Scrapy3ProxyMiddleware process_request 100")
        # Called for each request that goes through the downloader
        # middleware.

        sessid = f"sessid-{random.randint(1000000000, 9999999999)}"
        request.meta['proxy'] = f"http://customer-fenggen090909_jZYpf-{sessid}-sesstime-1:Fenggen285426_@pr.oxylabs.io:7777"


        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        logging.critical("fg middlewares Scrapy3ProxyMiddleware process_response 110")
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        logging.critical("fg middlewares Scrapy3ProxyMiddleware process_exception 120")
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        logging.critical("fg middlewares Scrapy3ProxyMiddleware spider_opened 130")
        spider.logger.critical("Spider opened: %s" % spider.name)

    def spider_closed(self, spider):
        logging.critical("fg middlewares Scrapy3ProxyMiddleware spider_closed 140")
        spider.logger.critical("Spider closed: %s" % spider.name)
    


class Scrapy3SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self):
        logging.critical("fg middlewares scrapy3SpiderMiddleware __init__ 10")
        pass

    @classmethod
    def from_crawler(cls, crawler):
        logging.critical("fg middlewares scrapy3SpiderMiddleware from_crawler 20")
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        logging.critical("fg middlewares scrapy3SpiderMiddleware process_spider_input 30")
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        logging.critical("fg middlewares scrapy3SpiderMiddleware process_spider_output 40")
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        logging.critical("fg middlewares scrapy3SpiderMiddleware process_spider_exception 50")
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        logging.critical("fg middlewares scrapy3SpiderMiddleware process_start_requests 60")
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        logging.critical("fg middlewares scrapy3SpiderMiddleware spider_opened 70")
        spider.logger.info("Spider opened: %s" % spider.name)

    def spider_closed(self, spider):
        logging.critical("fg middlewares scrapy3SpiderMiddleware spider_closed 80")
        spider.logger.info("Spider closed: %s" % spider.name)


class Scrapy3DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):
        logging.critical("fg middlewares scrapy3DownloaderMiddleware __init__ 85")
        pass

    @classmethod
    def from_crawler(cls, crawler):
        logging.critical("fg middlewares scrapy3DownloaderMiddleware from_crawler 90")
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        logging.critical("fg middlewares scrapy3DownloaderMiddleware process_request 100")
        # Called for each request that goes through the downloader
        # middleware.

        # logging.critical(f"fenggen request_ip={request.meta}")

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        logging.critical("fg middlewares scrapy3DownloaderMiddleware process_response 110")
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        logging.critical("fg middlewares scrapy3DownloaderMiddleware process_exception 120")
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        logging.critical("fg middlewares scrapy3DownloaderMiddleware spider_opened 130")
        spider.logger.critical("Spider opened: %s" % spider.name)

    def spider_closed(self, spider):
        logging.critical("fg middlewares scrapy3DownloaderMiddleware spider_closed 140")
        spider.logger.critical("Spider closed: %s" % spider.name)

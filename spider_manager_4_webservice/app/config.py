import os
import logging



class Config:

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    logging.info(f"fg config.py BASE_DIR: {BASE_DIR}")  # 调试信息


    # Redis URL
    REDIS_URL = 'redis://192.168.0.58:6379/0'
    
    # Flask配置
    SECRET_KEY = 'dev-key-for-testing'
    
    # Celery配置
    # BROKER_URL= REDIS_URL
    # RESULT_BACKEND= REDIS_URL

    broker_url= REDIS_URL
    result_backend= REDIS_URL
    
    # Scrapy项目路径 - 根据实际情况调整
    SCRAPY_PROJECT_PATH = '/app/spider_manager_4/scrapy_3'


    
    # SCRAPY_PROJECT_PATH = BASE_DIR  
    # print(f"SCRAPY_PROJECT_PATH: {SCRAPY_PROJECT_PATH}")  # 调试信息
    # FLASK_PROJECT_PATH = '/app/spider_manager_3'
    # SCRAPY_PROJECT_PATH = '/app/scrapy_3' 
    
    # 日志目录
    # LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
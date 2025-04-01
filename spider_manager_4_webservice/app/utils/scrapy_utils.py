import os
from app.config import Config
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import logging
from app.config import Config
import os
import importlib.util
import inspect
import sys
from app.utils.logger import get_logger

    
sys.path.append('/app') 

def get_spider_domains(scrapy_project_path):
    """获取所有爬虫对应的网站域名，通过多种方式尝试确定爬虫的网站"""
    
    # 正确设置 Python 路径
    import os
    import sys
    import logging
    import re
    import inspect
    from urllib.parse import urlparse
    import scrapy       
    
    original_path = sys.path.copy()
    
    # 确保 scrapy_project_path 在路径中
    sys.path.insert(0, scrapy_project_path)
    logging.info(f"fg ---scrapy_project_path={scrapy_project_path}")
    # logger.info(f"fg ---scrapy_project_path={scrapy_project_path}")
    print(f"fg ---scrapy_project_path={scrapy_project_path}")
    
    # 设置环境变量
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'scrapy_3.settings')
    
    try:
        try:
            import scrapy_3.settings
        except ImportError as e:
            logging.error(f"fg scrapy_utils 导入失败: {e}")
            return {}
        
        from scrapy.utils.project import get_project_settings
        from scrapy.crawler import CrawlerProcess
        
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        spider_names = process.spider_loader.list()
        
        # 获取爬虫对应的域名
        domain_to_spiders = {}
        # 存储可能的网站名称
        website_to_spiders = {}
        
        for spider_name in spider_names:
            logging.info(f"fg scrapy_utils spider_name={spider_name}")
            try:
                # 获取爬虫类
                spider_class = process.spider_loader.load(spider_name)
                # 创建爬虫实例
                try:
                    spider_instance = spider_class()
                except scrapy.exceptions.CloseSpider as e:
                    # 处理需要参数的爬虫
                    logging.warning(f"fg scrapy_utils 爬虫 {spider_name} 初始化时关闭: {e}")
                    
                    # 尝试分析爬虫类名称或模块名称来确定网站
                    module_name = spider_class.__module__.split('.')[-1]
                    if module_name != 'spiders':
                        # 如果模块名不是通用的'spiders'，可能是网站特定的
                        if module_name not in website_to_spiders:
                            website_to_spiders[module_name] = []
                        website_to_spiders[module_name].append(spider_name)
                    else:
                        # 从类名中提取可能的网站名称
                        class_name = spider_class.__name__.lower()
                        name_parts = re.split(r'[_\-]', class_name)
                        for part in name_parts:
                            if part not in ['spider', 'crawler', 'scraper', 'bot']:
                                if part not in website_to_spiders:
                                    website_to_spiders[part] = []
                                website_to_spiders[part].append(spider_name)
                                break
                            else:
                                # 如果无法确定，放入需要参数的分类
                                if "requires_params" not in website_to_spiders:
                                    website_to_spiders["requires_params"] = []
                                website_to_spiders["requires_params"].append(spider_name)
                    
                    # 跳过当前爬虫的其余处理
                    continue
                except Exception as e:
                    # 其他初始化错误
                    logging.warning(f"fg scrapy_utils 爬虫 {spider_name} 初始化失败: {e}")
                    if "initialization_failed" not in website_to_spiders:
                        website_to_spiders["initialization_failed"] = []
                    website_to_spiders["initialization_failed"].append(spider_name)
                    continue
                
                domain_found = False
                
                # 方法1: 尝试获取 allowed_domains 属性
                if hasattr(spider_instance, 'allowed_domains') and spider_instance.allowed_domains:
                    primary_domain = "".join(spider_instance.allowed_domains)
                    
                    # logging.info(f"fg scrapy_utils xxxx={type(spider_instance.allowed_domains)}")
                    logging.info(f"fg scrapy_utils xxx={spider_instance.allowed_domains} primary_domain={primary_domain }")
                    
                    if primary_domain not in domain_to_spiders:
                        domain_to_spiders[primary_domain] = []
                    
                    domain_to_spiders[primary_domain].append(spider_name)
                    domain_found = True
                    # logging.info(f"fg scrapy_utils domain_to_spiders={domain_to_spiders}")                                              
               
            
            except Exception as e:
                logging.error(f"fg scrapy_utils 处理爬虫 {spider_name} 时出错: {e}")
                import traceback
                logging.error(traceback.format_exc())    

        logging.info(f"domain_to_spiders={domain_to_spiders}")
        
        for el, spiders in domain_to_spiders.items():
            logging.info(f"fg scrapy_utils el={el}, spiders={spiders}")                        
        
        return domain_to_spiders           
    
    except Exception as e:
        logging.error(f"fg scrapy_utils 获取爬虫域名失败: {e}")
        import traceback
        logging.error(traceback.format_exc())
        return {}
    
    finally:
        # 恢复 Python 路径
        sys.path = original_path





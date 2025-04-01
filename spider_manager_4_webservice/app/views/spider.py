from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from app.utils.scrapy_utils import get_spider_domains
# from app.tasks.spider_tasks import run_spider_task
from app import celery
from app.config import Config
import os
import importlib.util
import inspect
import sys
from app.config import Config
import logging 
import requests
import json
from app.tasks.spider_tasks import run_crawler_task, get_worker_ip

# 创建蓝图
spider_bp = Blueprint('spider', __name__)

# celery = Celery('spider_tasks', 
#                 broker=Config.REDIS_URL,
#                 backend=Config.REDIS_URL)

# get domain list
@spider_bp.route('/domain_to_spiders')
def get_domain_list():

    logging.info(f"fg get_domain_list Config.SCRAPY_PROJECT_PATH={Config.SCRAPY_PROJECT_PATH}")
    # spiders = get_available_spiders(Config.SCRAPY_PROJECT_PATH)
    domain_to_spiders = get_spider_domains(Config.SCRAPY_PROJECT_PATH)

    return jsonify({'domain_to_spiders': domain_to_spiders})   


# @spider_bp.route('/run', methods=['POST'])
# def run_spider():

#     logging.info(f"fenggen views-spider run_spider start...")
#     """启动爬虫"""

#     data = request.get_json()
#     spider_name = data.get('spider_name')    

#     logging.info(f"fenggen --- spider_name={spider_name}")
    
#     # 启动爬虫任务
#     # 假设我们已经定义了run_crawler_task
    
#     # ip_result = get_worker_ip.delay().get()
#     # task = run_crawler_task.delay(spider_name)
    
#     return jsonify({
#         'status': 'success',
#         # 'task_id': task.id,
#         'message': f'Testing endpoint for spider {spider_name}'
#     })


@spider_bp.route('/run', methods=['POST'])
def run_spider():

    logging.info(f"fenggen views-spider run_spider start...")
    """启动爬虫"""

    data = request.get_json()
    spider_name = data.get('spider_name')    

    logging.info(f"fenggen --- spider_name={spider_name}")
    
    # 启动爬虫任务
    # 假设我们已经定义了run_crawler_task
    
    # get_worker_ip.apply_async(queue='producer_queue')  # 明确指定队列
    # task = run_crawler_task.delay(spider_name)
    task = run_crawler_task.apply_async(args=[spider_name], queue='producer_queue')
    
    return jsonify({
        'status': 'success',
        'task_id': task.id,
        'message': f'spider {spider_name} is running'
    })


# @spider_bp.route('/run', methods=['POST'])
# def run_spider():
#     logging.info(f"fg run_spider...")
#     data = request.get_json(silent=True)
#     spider_name = data.get('spider_name') if data else None
#     if not spider_name:
#         return jsonify({
#             'status': 'error', 
#             'message': 'spider_name is required'
#             }), 400
    
#     project_path = '/app/spider_manager_4/scrapy_3'
#     task = run_spider_task.delay(spider_name, project_path)
#     logging.info(f"Started spider '{spider_name}' with task ID {task.id}")
#     return jsonify({'status': 'success', 'task_id': task.id, 'message': f'Spider {spider_name} is running'})


# @spider_bp.route('/stop', methods=['POST'])
# def stop_spider():
#     data = request.get_json(silent=True)
#     task_id = data.get('task_id') if data else None
#     if not task_id:
#         return jsonify({'status': 'error', 'message': 'task_id is required'}), 400
    
#     celery_app.control.revoke(task_id, terminate=True)
#     logging.info(f"Stopped task '{task_id}'")
#     return jsonify({'status': 'success', 'message': f'Task {task_id} terminated'})
from flask import Blueprint, render_template, request, jsonify, url_for, redirect
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
# from app.tasks.spider_tasks import run_crawler_task, get_worker_ip

# 创建蓝图
spider_bp = Blueprint('spider', __name__)


@spider_bp.route('/run', methods=['POST'])
def run_spider():

    logging.info(f"fenggen views-spider run_spider start...")
    """启动爬虫"""

    data = request.get_json()
    spider_name = data.get('spider_name')    

    logging.info(f"fenggen --- spider_name={spider_name}")
    
    task = celery.send_task(
        'app.tasks.spider_tasks.run_crawler_task',  # 远程任务名称
        args=[spider_name],
        queue='producer_queue'
    )
    
    return jsonify({
        'status': 'success',
        'task_id': task.id,
        'message': f'spider {spider_name} is running'
    })


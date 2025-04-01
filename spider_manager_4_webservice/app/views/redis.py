from flask import Blueprint, render_template, jsonify, request
from celery.result import AsyncResult
from app import celery
import requests
import json
import logging
import redis


# 创建蓝图
redis_bp = Blueprint('redis', __name__)

# base on taskid and spidername
@redis_bp.route('/queue', methods=['POST'])
def get_redis_queue():
    logging.info(f"fg get_redis_queue start ")

    data = request.get_json()
    spider_name = data.get('spider_name') 
    task_id = data.get('task_id')   
    
    r = redis.Redis(host='192.168.0.58', port=6379, db=0)
    if spider_name in ['web11spider', 'web12spider']:
        queue_name = 'detail_url_queue'
    
    queue_length = r.llen(queue_name)
    queues_raw = r.lrange(queue_name, 0, -1)

    queues = []
    for item_bytes in queues_raw:
        item = json.loads(item_bytes.decode('utf-8'))  # 假设是JSON格式
        if item['taskid'] == task_id:  # 使用字典访问方式
            queues.append(item)    

    logging.info(f"fg queue_length={queue_length} queues={queues}")    
    
    return jsonify(queues)








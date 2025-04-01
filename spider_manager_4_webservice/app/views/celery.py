from flask import Blueprint, render_template, jsonify, request
from celery.result import AsyncResult
from app import celery
import requests
import json
import logging
import redis


# 创建蓝图
celery_bp = Blueprint('celery', __name__)


@celery_bp.route('/worker')
def get_worker_list():
    logging.info(f"fg get_worker_list start ")
    flower_url = 'http://192.168.0.58:5555'
    workers_raw = requests.get(f'{flower_url}/api/workers')
    logging.info(f"fg spider workers_raw={workers_raw}")

    workers = json.loads(workers_raw.text)
    logging.info(f"fg spider workers={workers}")

    return jsonify({'workers': workers})

@celery_bp.route('/task')
def get_task_list():
    logging.info(f"fg get_task_list start ")
    flower_url = 'http://192.168.0.58:5555'
    tasks_raw = requests.get(f'{flower_url}/api/tasks')
    tasks = json.loads(tasks_raw.text)
    logging.info(f"fg spider tasks={tasks}")

    return jsonify({'tasks': tasks})    


@celery_bp.route('/task_info')
def get_task_info():
    logging.info(f"fg get_task_info start ")
    flower_url = 'http://192.168.0.58:5555'
    
    data = request.get_json()
    task_id = data.get('task_id')   

    task_info_raw = requests.get(f'{flower_url}/api/task/info/{task_id}')
    task_info = json.loads(task_info_raw.text) 
    
    logging.info(f"fg spider tasks={task_info}")

    return jsonify({'task_info': task_info})    








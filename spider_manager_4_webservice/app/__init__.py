from flask import Flask, Blueprint, render_template, jsonify, redirect, url_for, request, Response
from celery import Celery
from app.config import Config
import logging
from datetime import datetime
import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST


# 初始化Celery
celery = Celery('spider_tasks', 
                broker=Config.REDIS_URL,
                backend=Config.REDIS_URL)

# 定义 Prometheus 指标 - Flask 部分
REQUEST_COUNT = Counter('flask_request_count', 'App Request Count', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Request latency', ['method', 'endpoint'])

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.template_filter('datetimeformat')
    def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
        if isinstance(value, (int, float)):
            return datetime.fromtimestamp(value).strftime(format)
        return value
    
    # 配置Celery
    celery.conf.update(app.config)
    celery.conf.update(broker_connection_retry_on_startup=True)

    # 添加 Prometheus 指标端点
    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    # 添加请求监控中间件
    @app.before_request
    def before_request():
        request.start_time = time.time()

    @app.after_request
    def after_request(response):
        request_latency = time.time() - request.start_time
        REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
        REQUEST_LATENCY.labels(request.method, request.path).observe(request_latency)
        return response

    from app.views.spider import spider_bp
    
    from app.views.celery import celery_bp
    from app.views.redis import redis_bp
    
    app.register_blueprint(spider_bp, url_prefix='/spider')    
    app.register_blueprint(celery_bp, url_prefix='/celery')
    app.register_blueprint(redis_bp, url_prefix='/redis') 
    
    # 注册一个简单的路由
    @app.route('/')
    def index():
        return redirect(url_for('spider.index'))
    
    return app
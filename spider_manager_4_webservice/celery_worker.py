from app import celery
# 显式导入任务模块，确保任务注册到Celery
from app.tasks import spider_tasks
from app.utils.logger import get_logger
from prometheus_client import Counter, Histogram, Gauge, push_to_gateway
from celery.signals import task_prerun, task_postrun
import time

logger = get_logger(__name__)

# 定义 Prometheus 指标
TASK_COUNT = Counter('celery_task_count', 'Celery Task Count', ['task_name', 'state'])
TASK_LATENCY = Histogram('celery_task_latency_seconds', 'Task latency', ['task_name'])
TASKS_RUNNING = Gauge('celery_tasks_running', 'Tasks Running', ['task_name'])

# 添加任务信号处理器
@task_prerun.connect
def task_prerun_handler(task_id, task, *args, **kwargs):
    logger.info(f"Task started: {task.name}[{task_id}]")
    TASKS_RUNNING.labels(task.name).inc()
    
@task_postrun.connect
def task_postrun_handler(task_id, task, *args, retval=None, state=None, **kwargs):
    logger.info(f"Task completed: {task.name}[{task_id}] with state {state}")
    TASK_COUNT.labels(task.name, state).inc()
    TASKS_RUNNING.labels(task.name).dec()
    try:
        # 推送指标到 Prometheus Pushgateway (如果使用)
        # 注意: 确保 prometheus:9091 是正确的 pushgateway 地址
        push_to_gateway('192.168.0.58:9091', job=task.name, registry=None)
    except Exception as e:
        logger.error(f"Error pushing metrics to gateway: {e}")


# 添加一个简单任务用于测试
@celery.task
def test_task(x, y):
    start_time = time.time()
    result = x + y
    # 手动记录任务执行时间
    task_latency = time.time() - start_time
    TASK_LATENCY.labels('test_task').observe(task_latency)
    return result
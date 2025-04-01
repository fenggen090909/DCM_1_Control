from app.utils.logger import get_logger
import os
from app import create_app

logger = get_logger(__name__)



# 记录一条启动日志
logger.info("应用启动中...")

# 创建 Flask 应用
app = create_app()


if __name__ == '__main__':
    logger.info("run.py 开始执行...")
    # 记录一些配置信息
    logger.info(f"SCRAPY_PROJECT_PATH={os.environ.get('SCRAPY_PROJECT_PATH', '未设置')}")
    app.run(debug=True, host='0.0.0.0')
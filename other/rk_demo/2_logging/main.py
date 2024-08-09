'''
注释掉的部分只是在此文件中使用
显示的部分可以当做模块使用
在 logging 模块中,日志处理分为以下几个层级:

Logger: 负责产生日志消息。每个 Logger 实例都有一个名称,通常表示日志消息的来源。
Handler: 负责处理日志消息的输出。比如将日志输出到控制台、文件、网络等。
Formatter: 负责格式化日志消息的输出格式。
Filter: 用于过滤日志消息,决定哪些消息应该被输出。
'''
# import logging

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

# logging.info("This is an informational message.")



import logging

LOG_FORMAT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 全局定义logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 创建一个处理器并设置格式
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

# 将处理器添加到logger
logger.addHandler(handler)

if __name__ == '__main__':
# 在任何地方都可以使用logger来记录日志

    logger.info("This is an informational message.")



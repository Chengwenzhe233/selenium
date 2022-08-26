from config.conf import ConfigManager
import logging

cm = ConfigManager()


class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            """创建一个handle写入文件"""
            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            """创建一个handle输出到控制台"""
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            """定义输出格式"""
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            """添加到handle"""
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

        """日志打印格式"""

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'


if __name__ == '__main__':
    log = Log().logger
    log.info('测试一下')

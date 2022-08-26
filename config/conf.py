import os
from selenium.webdriver.common.by import By
from utils.times import dt_strftime


class ConfigManager:
    """项目目录"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    """页面元素目录"""
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    """报告文件"""
    REPORT_FILE = os.path.join(BASE_DIR, 'report.html')

    "元素定位类型"
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime("%Y%m%d%H%M%S")))

    @property
    def ini_file(self):
        """配置目录"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


if __name__ == '__main__':
    test = ConfigManager()
    print(test.BASE_DIR)
    print(test.ELEMENT_PATH)
    print(test.REPORT_FILE)
    print(test.LOCATE_MODE)
    print(test.log_file)
    print(test.ini_file)

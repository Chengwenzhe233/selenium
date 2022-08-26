import os
import yaml
from config.conf import ConfigManager


cm = ConfigManager()


class Element:
    """获取元素"""

    def __init__(self, name):
        self.file_name = '{}.yaml'.format(name)
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("{} 文件不存在！".format(self.element_path))
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def getitem(self, item):
        """获取元素属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))


if __name__ == '__main__':
    element = Element('test')
    print(element.getitem('搜索按钮'))

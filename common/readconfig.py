from config.conf import ConfigManager
import configparser

cm = ConfigManager()


class ReadConfig:
    """读取配置文件"""
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(cm.ini_file, encoding='utf-8')

    def get(self, section, option):
        """获取配置参数"""
        return self.config.get(section, option)


if __name__ == '__main__':
    ini = ReadConfig()
    print(ini.get('driver_switch', 'switch'))
    print(ini.get('driver_switch', 'address'))

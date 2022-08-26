import re
import pytest
from utils.logger import Log
from common.readconfig import ReadConfig
from page_object.searchpage import SearchPage


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        search.get_url(ReadConfig().get("driver_switch", "address"))

    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        Log().logger.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['test_search.py'])

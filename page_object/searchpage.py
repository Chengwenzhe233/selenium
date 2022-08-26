from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('search')


class SearchPage(WebPage):
    """搜索类"""

    def input_search(self, content):
        """输入搜索"""
        self.input_text(search.getitem('搜索框'), txt=content)
        sleep(0.5)

    def click_search(self):
        """点击搜索"""
        self.is_click(search.getitem('搜索按钮'))

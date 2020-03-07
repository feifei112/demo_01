"""
首页
"""
from selenium.webdriver.common.by import By

from base import MpBasePage

# 元素定位
class LndesPage(MpBasePage):
    # 元素
    def __init__(self):
        super().__init__()
        # 内容管理
        self.content_manager = (By.XPATH, "//*[text()='内容管理']")
        # 文章管理
        self.article_manager = (By.XPATH, "//*[contains(text(),'发布文章')]")
    # 查找元素
    def find_content_manager(self):
        return self.find_elt(self.content_manager)

    def find_article_manager(self):
        return self.find_elt(self.article_manager)

# 操作类
class IndesProxy:
    def __init__(self):
        self.indes_page = LndesPage()
    def click_content_manager(self):
        self.indes_page.find_content_manager().click()
    def click_article_manager(self):
        self.indes_page.find_article_manager().click()
# 业务类
class IndexProxy:
    def __init__(self):
        self.indes_proxy = IndesProxy()
    # 去文章发布页面
    def to_publish_aritcle_page(self):
        self.indes_proxy.click_content_manager()
        self.indes_proxy.click_article_manager()
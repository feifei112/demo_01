"""
发布文章测试类
"""
from datetime import time

from selenium.webdriver.common.by import By

from base import MpBasePage, BaseHandle
from utils import DriverUtils,select_option
import time

class PublishAlPage(MpBasePage):
    def __init__(self):
        super().__init__()
        # 文章标题
        self.article_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # 文章富文本iframe
        self.iframe = (By.ID, "publishTinymce_ifr")
        # 文章内容
        self.article_content = (By.ID, "tinymce")
        # 文章封面
        self.article_cover = (By.XPATH, "//*[text()='自动']")
        # 选择频道
        self.select__channel = (By.CSS_SELECTOR, "[placeholder = '请选择']")
        # 选择频道选项
        self.select__channel_option = (By.XPATH, "//*[text()='区块链']")
        # 发表按钮
        self.publish_btn = (By.XPATH, "//*[text()='发表']")


    # 元素进行查找

    def find_article_title(self): # 文章标题
       return self.find_elt(self.article_title)
    # 文章富文本iframe

    def find_iframe(self):
        return self.find_elt(self.iframe)
    # 文章内容

    def find_article_content(self):
        return self.find_elt(self.article_content)

     # 文章封面
    def find_article_cover(self):
        return self.find_elt(self.article_cover)
    # # 选择频道
    def find_select__channel(self):
        return self.find_elt(self.select__channel)
    # 选择频道选项
    def find_select__channel_option(self):
        return self.find_elt(self.select__channel_option)
    # 发表按钮
    def find_publish_btn(self):
        return self.find_elt(self.publish_btn)

# 操作层的封装
class  PublishAlHandle(BaseHandle):
    # 始初化
    def __init__(self):
        self.publish_al_page = PublishAlPage()
        self.driver = DriverUtils.get_mp_drvier()

    # 输入文章标题
    def input_article_title(self,title):
        self.input_text(self.publish_al_page.find_article_title(),title)
    # 输入文章内容
    def input_article_content(self,text):
        # 文章富文本iframe
        self.driver.switch_to_frame(self.publish_al_page.find_iframe())
        time.sleep(2)
        # 输入文章信息
        self.input_text(self.publish_al_page.find_article_content(),text)
        # 返回默认页面 (退出房间)
        self.driver.switch_to.default_content()
    # 选择封面
    def choice_article_cover(self):
        self.publish_al_page.find_article_cover().click()
    # 选择频道
    def check_channel_option(self, channel_option, select_text):
        """
        :param channel_option:选项的文本信息
        :param select_text:下来框的placehodler的属性值
        :return:
        """
        select_option(driver=self.driver,
                      select_text=select_text, channel_option=channel_option)
    # 提交文章
    def click_publish_btn(self):
        self.publish_al_page.find_publish_btn().click()


# 业务层的封装
class PublishAlProxy:
    def __init__(self):
        self.publist_ai_handle = PublishAlHandle()

    def test_publish_aritcle(self,title,aritcle_content,option,select_text):
        # 输入文章标题
        self.publist_ai_handle.input_article_title(title)
        # 输入文章内容
        self.publist_ai_handle.input_article_content(aritcle_content)
        # 选择封面
        self.publist_ai_handle.choice_article_cover()
        # 选择频道
        self.publist_ai_handle.check_channel_option(channel_option=option,select_text=select_text)
        self.publist_ai_handle.click_publish_btn()



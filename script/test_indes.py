""""

"""
"""
mp登陆测试用例
"""
import pytest
from selenium.webdriver.common.by import By

from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order = 3)
class TestMpLogin:

    # pytest 类级别的初始化fixture
    def setup_class(self):
        # 定义浏览器驱动实例属性来存放自媒体的浏览器驱动对象
        self.driver = DriverUtils.get_mp_drvier()

        self.index_proxy = IndexProxy()
    # pytest 类级别的销毁fixture
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
        IndexProxy()

    # 测试方法
    def test_indes_proxy(self):
        self.index_proxy.to_publish_aritcle_page()

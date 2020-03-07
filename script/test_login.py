"""
mp登陆测试用例
"""
import pytest
from selenium.webdriver.common.by import By

from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtils, is_element_exist

@pytest.mark.run(order = 2)
class TestMpLogin:

    # pytest 类级别的初始化fixture
    def setup_class(self):
        # 定义浏览器驱动实例属性来存放自媒体的浏览器驱动对象
        self.driver = DriverUtils.get_mp_drvier()
        self.login_proxy = LoginProxy()
    # pytest 类级别的销毁fixture
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
        IndexProxy()

    # 测试方法
    def test01_mp_login(self):
        # 定义测试数据
        mobile = "13911111111"
        code = "246810"
        # 调用登陆的方法
        self.login_proxy.test_mp_login(mobile, code)
        # 执行断言
        is_element = is_element_exist(self.driver,"传智播客")
        assert is_element




"""
发布文章测试用例
"""
import time
import pytest

from page.index_page import IndexProxy
from page.publish_aritcle_page import PublishAlProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=4)
class TestPublish:
    # pytest 里面使用始初化
    def setup_class(self):
        self.driver = DriverUtils.get_mp_drvier()
        self.publist_al_proxy = PublishAlProxy()


    def teardown_class(self):
    # 5.关闭浏览器释放资源
        DriverUtils.quit_mp_driver()

    def test_publish(self):

        # 数据
        title = "你好呀{}".format(time.strftime("%Y%m%d%H%M%S"))
        aritcle_content = "你好呀{}".format(time.strftime("%Y%m%d%H%M%S"))
        option = "linux"
        select_text = "请选择"

        self.publist_al_proxy.test_publish_aritcle\
            (title,aritcle_content,option,select_text)
        # 断言
        is_element = is_element_exist(self.driver,"新增文章成功")
        assert is_element
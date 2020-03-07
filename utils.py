import selenium.webdriver



from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 公用的选择选项的方法
def select_option(driver, select_text, channel_option):
    # 点击频道元素
    channel_xpath = "[placeholder='{}']".format(select_text)
    driver.find_element(By.CSS_SELECTOR, channel_xpath).click()

    option_list = driver.find_elements(By.CSS_SELECTOR, ".el-select-dropdown__item span ")
    # 是否能找到元素吗？
    is_option = False
    for option_element in option_list:
        if option_element.text == channel_option:  #channel_option 传过的参数
            is_option = True  # 表示找了
            print("find{}元素选项".format(channel_option))
            option_element.click() # 如果找到了点击的动作
        #  如不匹配则鼠标悬浮并且按住箭头
        else:
            ActionChains(driver).move_to_element(option_element) \
                .send_keys(Keys.DOWN).perform()

    # 如果到最后都没有找到对应选项，则抛出找不到元素的异常
    if is_option is False:
        NoSuchElementException("can't find {} option element"
                                       .format(channel_option))




# 断言：判定这个元素是否存在
def is_element_exist(driver, element_text):
    """
    :param driver:驱动对象
    :param element_text: 用于xpath文本定位元素的局部文本信息
    :return:如能根据局部文本信息能找到元素则返回元素对象，如找不到元素对象则is_elementde为默认False
    """
    xpath_string = "//*[contains(text(),'{}')]".format(element_text) #根据文本定位的xpath表达式
    is_element = False
    try:
        is_element = driver.find_element(By.XPATH, xpath_string)
    except Exception as e:
        is_element = False
        raise e
    return is_element


class DriverUtils:
    # 自媒体浏览器驱动私有属性
    __mp_driver = None

    # 后台管理系统浏览器驱动私有属性
    __mis_driver = None

    # app驱动对象私有属性
    __app_driver = None

    # 自媒体浏览器关闭的开关
    __mp_key = True
    # 自媒体获取浏览器驱动
    @classmethod
    def get_mp_drvier(cls):
        if cls.__mp_driver is None:
            # 实例化浏览器驱动对象
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.implicitly_wait(30)
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # 自媒体关闭浏览器驱动
    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver is not None and cls.__mp_key:
            cls.get_mp_drvier().quit()
            cls.__mp_driver = None

    # 修改自媒体开关的方法
    @classmethod
    def change_mp_key(cls,open_key):
        cls.__mp_key = open_key





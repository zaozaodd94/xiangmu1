#1定义测试类
import logging
import time

from parameterized import parameterized

from Page.mp.login_page import LoginPorxy
from utils import DriverUtils, element_is_exist, build_data
import pytest
@pytest.mark.run(order = 2 )
class TestLogin:

    #2定义初始化的方法
    def  setup_class(self):
        #获取自媒体但浏览器驱动对象并且赋给driver的实例属性
        self.driver = DriverUtils.get_mp_driver()
        #创建业务层对象
        self.login_proxy = LoginPorxy()
    #3定义销毁放f方法
    def teardown_class(self):
        #关闭浏览器
        time.sleep(2)
        DriverUtils.quit_mp_driver()
    @parameterized.expand(build_data)
    #4定义测试方法
    def test_login(self,mobile,code):
        # # 5定义测试数据
        # mobile = "15811859004"
        # code = "246810"
        # #6调用业务方法
        logging.info("{}y用户开始执行登录".format(mobile))
        self.login_proxy.test_login(mobile,code)
        # #7执行断言结果
        logging.info("开始执行打印，断言")
        is_suc = element_is_exist(driver=self.driver,text="江苏传智播客教育科技")
        assert is_suc
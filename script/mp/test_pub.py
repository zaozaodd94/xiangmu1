#1.定义测试类
import time

from Page.mp.home_page import HomePorxy
from Page.mp.publish_page import PubProxy
from config import BASE_ARITCAL_TITLE
from utils import DriverUtils, element_is_exist
import pytest
@pytest.mark.run(order =3 )
class TestPubAritical:
    #2.电仪累计被初始化方法
    def setup_class(self):
        #打开浏览器
        self.driver = DriverUtils.get_mp_driver()
        #创建所需要的页面的业务层对象
        self.home_proxy = HomePorxy()
        self.pub_proxy = PubProxy()
    #3.定义累计被销毁方法
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
    #4.定义测试方法
    def test_pub_aritical(self):
        #5.定义组织数据
        title = BASE_ARITCAL_TITLE
        content = "想要一辆法拉利"
        option = "数码产品"
        #6.调用业务层的方法
        self.home_proxy.to_publish_page()
        self.pub_proxy.test_pub_aritcal(title,content,option)
        #7.断言实际结果"新增文章成功"
        is_suc = element_is_exist(driver=self.driver,text="新增文章成功")
        assert is_suc
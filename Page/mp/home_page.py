#自媒体主页
from selenium.webdriver.common.by import By

from Base.mp.base_page import BasePage, BaseHandle


#对象层
class HomePage(BasePage):
    #1定义初始化方法f
    def __init__(self):
        super().__init__()
        #2将所需要的操作的元素定义一个对应的实例属性

        # 3实例属性存储元素定位一级对应值
        #内容管理
        self.content_manager = (By.XPATH,"//*[text()='内容管理']")
        self.publish_artical =(By.XPATH,"//*[contains(text(),'发布文章')]")
     # 4定义找所有元素的实例方法
    def find_content_manager(self):
        return self.find_elt(self.content_manager)
    def find_publish_artical(self):
        return self.find_elt(self.publish_artical)

#操作成
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page  = HomePage()
    #点击内容管理
    def click_content_manager(self):
        self.home_page.find_content_manager().click()
    #点击发布文章
    def click_publish_artical(self):
        self.home_page.find_publish_artical().click()


#业务层
class HomePorxy:
    def __init__(self):
        self.home_handle = HomeHandle()
    #进入发布文章页面
    def to_publish_page(self):
        #1.点击内容管理
        self.home_handle.click_content_manager()
        #点击发布文章
        self.home_handle.click_publish_artical()
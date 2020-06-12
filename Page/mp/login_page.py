from selenium.webdriver.common.by import By

from Base.mp.base_page import BasePage, BaseHandle




# 对象层
class LoginPage(BasePage):

    # 1定义初始化方法f
    def __init__(self):
        super().__init__()
        # 将所需要的操作的元素定义一个对应的实例属性
        self.moblie = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        # 验证码
        self.code = (By.CSS_SELECTOR, '[placeholder="验证码"]')
        # 登录按钮
        # 3实例属性存储元素定位一级对应值
        self.login_bth = (By.CSS_SELECTOR, ".el-button--primary")

    # 4定义找所有元素的实例方法
    def find_moblie(self):
        return self.find_elt(self.moblie)

    def find_code(self):
        return self.find_elt(self.code)

    def find_login_bth(self):
        return self.find_elt(self.login_bth)


# 操作成
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 手机号码输入
    def input_moblie(self, moblie):
        self.input_text(self.login_page.find_moblie(), moblie)

    # 验证码输入
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 点击登录
    def click_login_bth(self):
        self.login_page.find_login_bth().click()


# 业务层
class LoginPorxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # d登录操作方法
    def test_login(self, mobile, code):
        # 1.输入手机号码
        self.login_handle.input_moblie(mobile)
        # 2.输入验证码
        self.login_handle.input_code(code)
        # 3.点击登录按钮
        self.login_handle.click_login_bth()

from selenium.webdriver.common.by import By

from aapctests.LoginPage import LoginPage
from aapctests.schedule import Scheduleexam
from testss.BaseClass2 import Baceclass

class TestLogin(Baceclass):
    def test_login(self):
        login = LoginPage(self.driver)
        login.getlogin().click()
        login.getusername().send_keys("ashu@gmail.com")
        login.getpassword().send_keys("Apple@12345")
        login.getloginbtn().click()

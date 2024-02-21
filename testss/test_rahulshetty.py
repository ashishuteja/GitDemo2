from aapctests.rshetty import Practice
from testss.BaseClass2 import Baceclass


class TestLogin(Baceclass):

    def test_login(self):
        login = Practice(self.driver)
        login.getlogin()


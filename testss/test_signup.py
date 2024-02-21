import time

from aapctests.LoginPage import LoginPage
from testss.BaseClass2 import Baceclass
from aapctests.signuppage import SignUppage


class TestAapc(Baceclass):
    def test_aapcsignup(self):

        aapcs = SignUppage(self.driver)
        aapcs.getsignup().click()
        aapcs.getFirstName().send_keys("meri")
        #time.sleep(10)
        aapcs.getLastname().send_keys("aashiqio")
        #time.sleep(20)
        aapcs.getEmail().send_keys("uyuyu@gmaill.com")
        aapcs.getNewpaswrd().send_keys("Apple@12345")
        time.sleep(10)
        aapcs.getSignupbtn().click()

        time.sleep(20)
        #self.driver.refresh()





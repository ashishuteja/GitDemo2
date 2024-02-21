from selenium.webdriver.common.by import By

from testss.conftest import driver


class LoginPage:

    def __init__(self, driver):
        self.driver = driver


    signinbuton = (By.ID,"btnSignIn")
    username = (By.ID,"signInName")
    password = (By.ID,"password")
    loginbtn = (By.ID,"continue")
    def getlogin(self):
        return driver.find_element(*LoginPage.signinbuton)
    def getusername(self):
        return driver.find_element(*LoginPage.username)
    def getpassword(self):
        return driver.find_element(*LoginPage.password)
    def getloginbtn(self):
        return driver.find_element(*LoginPage.loginbtn)




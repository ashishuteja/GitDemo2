from selenium.webdriver.common.by import By
from testss.conftest import driver



class SignUppage:

    def __init__(self, driver):
        self.driver = driver

    signup =(By.CLASS_NAME,"prenav-signin-signup")
    FirstName = (By.XPATH,"//input[@id = 'givenName']")
    LastName = (By.ID,"surname")
    Email = (By.ID,"email")
    NewPaswrd = (By.ID,"newPassword")
    Signupbtn = (By.ID,"continue")

    def getsignup(self):
        #driver.find_element(By.CLASS_NAME,"prenav-signin-signup").click()#we can use this as well
        return driver.find_element(*SignUppage.signup)

    def getFirstName(self):
        return driver.find_element(*SignUppage.FirstName)
    def getLastname(self):
        return driver.find_element(*SignUppage.LastName)
    def getEmail(self):
        return driver.find_element(*SignUppage.Email)

    def getNewpaswrd(self):
        return driver.find_element(*SignUppage.NewPaswrd)
    def getSignupbtn(self):
        return driver.find_element(*SignUppage.Signupbtn)

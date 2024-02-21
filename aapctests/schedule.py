from selenium.webdriver.common.by import By
from testss.conftest import driver
class Scheduleexam:
    def __init__(self, driver):
        self.driver = driver

    exam = (By.XPATH,"//body/form[@id='aspnetForm']/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[4]/a[1]")
    schexam = (By.PARTIAL_LINK_TEXT,"Schedule an exam")
    schexam1 = (By.XPATH,"//div[@id='ctl00_Body_conditionalCards0']")
    CPC = (By.XPATH,"//button[@value='CPC']")
    nextbuttn = (By.XPATH,"//button[@id='credential']")
    selectexampackage = (By.XPATH,"//form/div[2]/div[2]/div[1]/input")
    nextbutton = (By.XPATH,"//form/div[3]/button[2]")
    selectradiobutton = (By.XPATH,"//form/div[2]/div[3]/div[2]/div[1]")
    nextbutton2 = (By.XPATH,"//div[@class='flex justify-between pt-6']/button[2]")
    nextbutton3 = (By.XPATH,"//div[@class='flex justify-between pt-6']/button[2]")
    placeorder = (By.XPATH,"//div[@id='btnPlaceOrder']/span/input[1]")
    savebutton = (By.XPATH,"//div[@class='col-md-12']/a")




    def getexamlink(self):
        return self.driver.find_element(*Scheduleexam.exam)

    def getschedule(self):
        return driver.find_element(*Scheduleexam.schexam)

    def getschedule1(self):
        return driver.find_element(*Scheduleexam.schexam1)
    def getCPC(self):
        return driver.find_element(*Scheduleexam.CPC)

    def getnextbtn(self):
        return driver.find_element(*Scheduleexam.nextbuttn)

    def getexampackage(self):
        return driver.find_element(*Scheduleexam.selectexampackage)

    def getnextbutton(self):
        return driver.find_element(*Scheduleexam.nextbutton)
    def getradiobutton1(self):
        return  driver.find_element(*Scheduleexam.selectradiobutton)

    def getnextbutton2(self):
        return driver.find_element(*Scheduleexam.nextbutton2)

    def getnextbutton3(self):
        return driver.find_element(*Scheduleexam.nextbutton3)



    def getplaceorder(self):
        return driver.find_element(*Scheduleexam.placeorder)

    def getsavebutton(self):
        return driver.find_element(*Scheduleexam.savebutton)



        # def checkassertion(self):
        #condition = driver.find_element(By.LINK_TEXT, "Terms and Conditions").text
        #assert "Terms" in condition




    #def getexampackage(self):
       # exampackage = driver.find_elements(By.XPATH, "//div[@class='flex items-center']/input/)]")

       # for i in exampackage:
       #     if i.get_attribute("name")=="bestValueExam":
       #         i.click()
       #         assert i.is_selected()

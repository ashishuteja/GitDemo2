import time

from aapctests.schedule import Scheduleexam
from testss.BaseClass2 import Baceclass


class TestExam(Baceclass):
    def test_scheduleexam(self):
        exam = Scheduleexam(self.driver)
        exam.getexamlink().click()
        exam.getschedule().click()
        exam.getschedule1().click()
        exam.getCPC().click()
        exam.getnextbtn().click()
        #exam.getexampackage()
        exam.getexampackage().click()
        exam.getnextbutton().click()
        exam.getradiobutton1().click()
        exam.getnextbutton2().click()
        exam.getnextbutton3().click()
        exam.getplaceorder().click()
        exam.getsavebutton().click()

        time.sleep(60)
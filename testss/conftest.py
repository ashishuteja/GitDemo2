import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service= service_obj)


@pytest.fixture(scope="class")

def setup(request):

    driver.get("https://www.aapc.com")
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element(By.ID,"btnSignIn").click()
    driver.find_element(By.ID, "signInName").send_keys("ashu@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Apple@12345")
    driver.find_element(By.ID, "continue").click()
    #driver.get("https://rahulshettyacademy.com/angularpractice/")
    #driver.implicitly_wait(10)
    #driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(10)
    driver.close()
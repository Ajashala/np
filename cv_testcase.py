import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
driver.get("https://np.chimpvine.com/login/")
time.sleep(10)
#driver.find_element_by_name("username").send_keys("pramod")
#driver.find_element_by_name("password").send_keys('Pramod12!@')
#driver.find_element_by_id("login-submit").click()
driver.find_element(By.NAME, "username").send_keys("pramod")
driver.find_element(By.NAME, "password").send_keys("Pramod12!@")
driver.find_element(By.ID, "login-submit").click()

web_title = driver.title
time.sleep(10)
actual_title ="ChimpVine: Log in to the site"
if web_title== actual_title:
    print("login passed")
else:
    print("login failed")
#driver.close()
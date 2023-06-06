from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
driver.get("https://np.chimpvine.com/")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "dn-lg").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#login_username").send_keys("pramod")
#same class name so used "id' for password
driver.find_element(By.CSS_SELECTOR, "#login_password").send_keys("Pramod12!@")
driver.find_element(By.ID, "login-submit").click()
time.sleep(5)
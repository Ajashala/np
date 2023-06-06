from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
driver.get("https://np.chimpvine.com/")
driver.implicitly_wait(0.1)
element = driver.find_element(By.CLASS_NAME, "dn-lg")
element.click()
#driver.find_element(By.CLASS_NAME, "dn-lg").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@class='form-control poppins']").send_keys("pramod")
#same class name so used "id' for password
driver.find_element(By.XPATH, "//input[@class='form-control poppins' and @id='login_password']").send_keys("Pramod12!@")
driver.find_element(By.ID, "login-submit").click()
time.sleep(5)
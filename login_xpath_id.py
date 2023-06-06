from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Edge(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
driver.get("https://np.chimpvine.com/")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dn-lg")))
element.click()
#driver.find_element(By.CLASS_NAME, "dn-lg").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='login_username']").send_keys("pramod")
driver.find_element(By.XPATH, "//input[@id='login_password']").send_keys("Pramod12!@")
driver.find_element(By.ID, "login-submit").click()
time.sleep(5)
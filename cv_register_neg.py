from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
driver.get("https://np.chimpvine.com/")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "dn-lg").click()
driver.find_element(By.XPATH, value='//a[@href="https://np.chimpvine.com/login/signup.php"]').click()
driver.find_element(By.NAME, "email").send_keys("pramod111.com")
driver.find_element(By.NAME, "username").send_keys("pramodkharel112")
driver.find_element(By.NAME, "password").send_keys("Admin@123")
driver.find_element(By.ID, "id_confirm_password").send_keys("Admin@123")
driver.find_element(By.NAME, "agree").click()
driver.find_element(By.ID, "register-submit").click()
time.sleep(5)
#login_page
driver.find_element(By.NAME, "username").send_keys("pramod")
driver.find_element(By.NAME, "password").send_keys("Pramod12!@")
driver.find_element(By.ID, "login-submit").click()
current_url = driver.current_url
print("Current URL:", current_url)
web_title = driver.title
print("web title:",web_title)
time.sleep(10)
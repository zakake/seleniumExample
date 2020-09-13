from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/login")

# Input username
driver.find_element(by=By.ID, value="username").send_keys("tomsmith")
# Input password
password = driver.find_element(by=By.ID, value="password")
password.send_keys("SuperSecretPassword!")
# Submit form
password.submit()

time.sleep(5)
driver.quit()
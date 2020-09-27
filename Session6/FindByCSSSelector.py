from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

username = driver.find_element_by_css_selector("#email")
password = driver.find_element(By.CSS_SELECTOR, "#pass")

username.send_keys("abc@gmail.com")
password.send_keys("123456")

time.sleep(5)

driver.close()




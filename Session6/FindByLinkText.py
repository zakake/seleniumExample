from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

forget_password = driver.find_element_by_link_text("Quên mật khẩu?")

forget_password.click()

time.sleep(5)

driver.close()





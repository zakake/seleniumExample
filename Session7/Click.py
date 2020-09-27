from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

login_button = driver.find_element_by_name("login")

login_button.click()

time.sleep(5)

driver.close()




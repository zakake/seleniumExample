from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

slogan = driver.find_element_by_tag_name("h2")

print(slogan.text)

driver.close()






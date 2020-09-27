from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

elements = driver.find_elements_by_xpath("//*[@id=\"u_0_a\"]/div[1]/div/input")

print(len(elements))

for element in elements:
    print(element.get_attribute("placeholder"))

driver.close()




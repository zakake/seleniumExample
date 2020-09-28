from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("http://demo.guru99.com/test/drag_drop.html")

drag_location = driver.find_element(by=By.XPATH, value="//*[@id='fourth']")
drop_location = driver.find_element(by=By.XPATH, value="//*[@id='shoppingCart4']/div")
ActionChains(driver).drag_and_drop(drag_location, drop_location).perform()

time.sleep(5)
driver.quit()

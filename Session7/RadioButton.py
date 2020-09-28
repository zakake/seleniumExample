from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio")

driver.switch_to.frame(driver.find_element_by_id("iframeResult"))

male = driver.find_element_by_id("male")
female = driver.find_element_by_id("female")
other = driver.find_element_by_id("other")

time.sleep(2)

male.click()

time.sleep(2)

female.click()

time.sleep(2)

other.click()

time.sleep(2)

driver.close()
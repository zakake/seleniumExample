from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element_by_xpath("//*[@id=\"checkboxes\"]/input[1]")
checkbox2 = driver.find_element_by_xpath("//*[@id=\"checkboxes\"]/input[2]")

time.sleep(2)

if not checkbox1.is_selected():
    checkbox1.click()

if checkbox2.is_selected():
    checkbox2.click()

time.sleep(2)

driver.close()
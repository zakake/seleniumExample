from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")
# Open new window
driver.find_element(by=By.ID, value="openwindow").click()
# Switch to new window
driver.switch_to.window(driver.window_handles[1])
driver.maximize_window()
time.sleep(2)
# Switch to main windows
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://learn.letskodeit.com/p/practice")
# Open popup
driver.find_element(by=By.ID, value="name").send_keys("selenium")
driver.find_element(by=By.ID, value="confirmbtn").click()
#Switch to popup
popup = driver.switch_to.alert
print(popup.text)
time.sleep(2)
popup.accept()

time.sleep(2)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Page
driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get('https://learn.letskodeit.com/p/practice')

# Hide textbox
hide_button = driver.find_element(by=By.ID, value="hide-textbox")
hide_button.click()

# Try to set text to textbox is hidden
displayed_textbox = driver.find_element(by=By.ID, value="displayed-text")
# displayed_textbox.send_keys("abcd")

# Using Javascript
driver.execute_script("arguments[0].value = 'abcd'", displayed_textbox)



# Show textbox
show_button = driver.find_element(by=By.ID, value="show-textbox")
show_button.click()

time.sleep(5)
driver.close()

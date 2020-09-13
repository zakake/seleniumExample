from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.get("https://www.google.com")

search_box = driver.find_element_by_name('q')  # Find search input box.
search_box.send_keys('selenium')  # Type in selenium.
time.sleep(1)

# Select the 3rd options from the autocomplete.
driver.switch_to.active_element

search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(1)
search_box.send_keys(Keys.ARROW_DOWN)  # Press ARROW_DOWN key.
time.sleep(3)

# Search
search_box.send_keys(Keys.ENTER)
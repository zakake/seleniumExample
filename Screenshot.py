from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Page
driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get('https://learn.letskodeit.com/p/practice')

# Capture element screenshot
mouse_hover_element = driver.find_element(by=By.ID, value="mousehover")
mouse_hover_element.screenshot('mouseHover.png')

driver.quit()
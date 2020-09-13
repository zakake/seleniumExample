from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.get('http://the-internet.herokuapp.com/dropdown')

select = Select(driver.find_element_by_id('dropdown'))

# select by visible text
select.select_by_visible_text('Option 1')
time.sleep(5)
# select by value 
select.select_by_value('2')
time.sleep(5)
driver.close()
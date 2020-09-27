from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

username = driver.find_element_by_id("email")
password = driver.find_element(By.ID, "pass")

print(username.is_enabled())
print(password.is_enabled())

driver.close()





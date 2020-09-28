from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

# Get text on element
email_hint = driver.find_element(by=By.ID, value="email").get_attribute("aria-label")
print(email_hint)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.get("https://www.facebook.com/")

# Get text on element
slogan = driver.find_element(by=By.XPATH, value="//*[@id='content']/div/div/div/div[1]/h2").text
print(slogan)

driver.quit()


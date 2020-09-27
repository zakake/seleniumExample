from selenium import webdriver

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("http://automationpractice.com/index.php")

driver.quit()



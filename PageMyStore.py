import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

class PageMyStore(unittest.TestCase):
    def setUp(self):
        #Create webdriver instance
        self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        self.driver.implicitly_wait(5)
        #Open page
        self.driver.get("http://automationpractice.com/index.php")
        self.wait = WebDriverWait(self.driver, 10)
        #Waiting for My Store page is loaded
        self.wait.until(EC.title_contains("My Store"))

    def test_SignIn(self):
        #Click Sign in button
        signIn_button = self.driver.find_element_by_class_name("login")
        signIn_button.click()
        #Waiting for Login page is loaded
        self.wait.until(EC.title_contains("Login"))
        #Input email
        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys("uiabc@gmail.com")
        #Input passwords
        password_input = self.driver.find_element_by_id("passwd")
        password_input.send_keys("12345678")
        #Click submit button
        submit_button = self.driver.find_element_by_id("SubmitLogin")
        submit_button.click()
        #Waiting for My Account page is loaded
        self.wait.until(EC.title_contains("My account"))
        actualMessage = self.driver.find_element_by_class_name("info-account")
        expectedMessage = "Welcome to your account. Here you can manage all of your personal information and orders."
        #Verify login successfully
        self.assertEqual(actualMessage.text, expectedMessage,"passed")
    
    def test_Search(self):
        #Input search text
        search_input = self.driver.find_element_by_id("search_query_top")
        search_input.send_keys("Blouse")
        #Click search button
        search_button = self.driver.find_element_by_name("submit_search")
        search_button.click()
        #Wait for Search Result page is loaded
        self.wait.until(EC.title_contains("Search"))
        actualMessage= self.driver.find_element_by_class_name("heading-counter")
        expectedMessage = "1 result has been found."
        #Verify searh result
        self.assertEqual(actualMessage.text, expectedMessage)

    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     unittest.main(verbosity=2)

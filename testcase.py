import unittest
from appium import webdriver
#from appium.webdriver.common.mobileby import MobileBy
import random
import string
#from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"appium:deviceName": "emulator-5554",
	"platformName": "Android",
	"appium:appPackage": "com.google.android.contacts",
	"appium:appActivity": "com.android.contacts.activities.PeopleActivity",
	"appium:automationName": "UiAutomator2",
	"appium:noReset": "true",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
    
})
# Helper function to generate a random string
def random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))
def generate_phone_number():
    # Start with a digit between  6 and  9
    phone_number = str(random.randint(6,  9))
    # Append nine more random digits between  0 and  9
    for _ in range(9):
        phone_number += str(random.randint(0,  9))
    return phone_number
class ContactCreationTest(unittest.TestCase):
    def setUp(self):
        # Setup Appium driver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

    def tearDown(self):
        # Quit the driver after each test
        self.driver.quit()

    def test_create_contact(self):
        # Navigate to the contact creation page
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
        el2.click()

        # Generate random data for the contact fields
        first_name = random_string(5)
        last_name = random_string(5)
        company = random_string(10)
        phone = generate_phone_number()

        # Fill in the contact details
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"First name\"]")
        el3.send_keys("ass")

        el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Last name\"]")
        el4.send_keys("bakele")

        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Company\"]")
        el5.send_keys(company)

        el7 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Phone\"]")
        el7.send_keys(phone)
        # Save the contact
        el8 = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
        el8.click()

        el9 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
        el9.click()
        # Check that the contact was saved successfully
        # You might need to add additional checks based on your app's behavior
        #self.assertTrue(some_condition)
    # def test_edit_contact(self):
    #         # Navigate to the contact creation page
    #         company = random_string(10)
    #         phone = generate_phone_number()
    #         el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="ass bakele")
    #         el1.click()
    #         time.sleep(5)
    #         el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Edit contact")
    #         el2.click()
    #         time.sleep(5)
    #         el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"193mRAsOOJ\"]")
    #         el3.click()
    #         el3.send_keys(company)
    #         time.sleep(5)
    #         el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"(829) 556-5150\"]")
    #         el4.click()
    #         el4.send_keys(phone)
    #         # el5 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Email\"]")
    #         # el5.click()
    #         # el5.send_keys("test@test.com")
    #          # Save the contact
    #         time.sleep(5)
    #         el6 = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
    #         el6.click()
    #         time.sleep(5)
    #         el7 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
    #         el7.click()
    def test_delete_contact(self):
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="ass bakele")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="More options")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.google.android.contacts:id/title\" and @text=\"Delete\"]")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        el4.click()

if __name__ == '__main__':
    unittest.main()

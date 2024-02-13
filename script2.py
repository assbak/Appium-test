from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import random
import string
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

def random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

# Assuming the driver setup and connection to Appium server is already done
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
el2.click()

# el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
# el1.click()
# el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
# el2.click()
# el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"First name\"]")
# el3.click()
# el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Last name\"]")
# el4.click()
# el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Company\"]")
# el5.click()
# el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Company\"]")
# el6.click()
# el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Phone\"]")
# el7.click()
# el8 = driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
# el8.click()
# el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
# el9.click()

first_name = random_string(5)
last_name = random_string(5)
company = random_string(10)
phone = random_string(10)

el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"First name\"]")
el3.send_keys(first_name)

el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Last name\"]")
el4.send_keys(last_name)

el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Company\"]")
el5.send_keys(company)

el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Phone\"]")
el7.send_keys(phone)

el8 = driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
el8.click()

el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el9.click()

driver.quit()
# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

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
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
el9.click()
el10 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"First name\"]")
el10.click()
el11 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Last name\"]")
el11.click()
el12 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Company\"]")
el12.click()
el13 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Phone\"]")
el13.click()
el14 = driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
el14.click()
el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el15.click()

driver.quit()
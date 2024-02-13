import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import HtmlTestRunner
import time
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
@pytest.fixture
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "appium:deviceName": "emulator-5554",
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "C:\\Users\\Administrateur\\Documents\\GitHub\\Appium-test\\ExpenseManager_1.7.apk",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    driver.implicitly_wait(20)
    yield driver

    driver.quit()


def test_add_income(driver):
    el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.webkit.WebView")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Consent\"]")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/addIncBtn")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/btnTwo")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/btnFive")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/btnZero")
    el6.click()
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/btnDone")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/categoryTV")
    el8.click()
    el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.moneytower.expmngr:id/text\" and @text=\"Salary\"]")
    el9.click()
    el10 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/accountTV")
    el10.click()
    el11 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/accName")
    el11.click()
    el12 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/payeeET")
    el12.click()
    el12.send_keys("assb")
    el13 = driver.find_element(by=AppiumBy.ID, value="com.moneytower.expmngr:id/saveBtn")
    el13.click()

    
    #pour lancer l'exécution et générer un rapport avec
    #pytest --html=report.html .\Expence_apk_test_pytest.py



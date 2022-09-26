from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.webelement import WebElement
from config import CREDENTIALS
from time import sleep
import elements
import subprocess


def str2bool(str):
    if (str == 'true'):
        return True
    elif (str == 'false'):
        return False
    else:
        raise TypeError(f'Cannot convert string with value "{str}" to bool')


class AutobonusDriver():

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = '/home/antiss/Downloads/life.apk'
        desired_caps['appium:appWaitForLaunch'] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)
        self.login()
        sleep(5)

        # If app requires protection method - select None
        protection_title_element = self.get_element(
            value='by.com.life.lifego:id/main_screen_text', type='id')
        protection_title_text = protection_title_element.get_attribute('text')
        if protection_title_text == 'Защитить Мой life:)':
            # Select None
            self.get_element(
                value=elements.RADIOS['APP_PROTECTION_METHOD_NONE_XPATH'], type='xpath').click()
            self.get_element(
                value=elements.BUTTONS['NEXT_ID'], type='id').click()
        sleep(5)

        # Click on the first icon in the hotbar (by default it is bonus action)
        self.get_element(
            value='by.com.life.lifego:id/first_button', type='id').click()
        subprocess.run("./shake.sh")

    def login(self):
        # If popup asking app notifications right has place - deny
        notifications_pushup = self.get_element(
            value=elements.BUTTONS['NOTIFICATIONS_DENY_ID'], type='id')
        if (notifications_pushup):
            notifications_pushup.click()

        # If login requires - type login and password
        phone_field = self.get_element(
            value=elements.FIELDS['PHONE_ID'], type='id')
        if not phone_field:
            return

        self.input_text(phone_field, CREDENTIALS['LOGIN'])
        self.input_text(
            elements.FIELDS['PASSWORD_ID'], CREDENTIALS['PASSWORD'])

        # Save password in app
        keepPasswordCheckbox = self.driver.find_element(
            by=AppiumBy.ID, value=elements.CHECKBOXES['KEEP_PASSWORD_ID'])
        isChecked = str2bool(keepPasswordCheckbox.get_attribute('checked'))
        if not isChecked:
            keepPasswordCheckbox.click()

        # Click login button
        self.get_element(
            value=elements.BUTTONS['LOGIN_ID'], type='id').click()

    def get_element(self, type, value):
        try:
            if (type == 'id'):
                return self.driver.find_element(by=AppiumBy.ID, value=value)
            elif (type == 'xpath'):
                return self.driver.find_element(by=AppiumBy.XPATH, value=value)
        except NoSuchElementException:
            return False

    def input_text(self, where, type, text):
        if (isinstance(where, WebElement)):
            where.send_keys(text)
        else:
            self.get_element(type=type, value=where).send_keys(text)


if __name__ == '__main__':
    app = AutobonusDriver()
    app.setUp()

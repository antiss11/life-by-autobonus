from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.webelement import WebElement
from config import CREDENTIALS
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        sleep(10)
        self.login()
        sleep(5)

        # If app requires protection method - select None
        protection_title_element = self.get_element_with_wait(
            elements.TEXT["APP_PROTECTION_METHOD_TITLE_ID"], timeout=30
        )
        protection_title_text = protection_title_element.get_attribute("text")
        if protection_title_text == "Защитить Мой life:)":
            # Select None
            self.get_element_with_wait(
                elements.RADIOS["APP_PROTECTION_METHOD_NONE_XPATH"], type="XPATH"
            ).click()
            self.get_element_with_wait(elements.BUTTONS["NEXT_ID"]).click()

        # Click on the first icon in the hotbar (by default it is bonus action)
        self.get_element_with_wait(
            elements.BUTTONS["HOTBAR_FIRST_ID"], timeout=20
        ).click()

        sleep(5)
        subprocess.run("./shake.sh")

    def login(self):
        # If popup asking app notifications right has place - deny
        notifications_pushup = self.get_element_with_wait(
            elements.BUTTONS["NOTIFICATIONS_DENY_ID"], timeout=10
        )
        if notifications_pushup:
            notifications_pushup.click()

        # If login requires - type login and password
        phone_field = self.get_element_with_wait(elements.FIELDS["PHONE_ID"])
        if not phone_field:
            return

        self.input_text(phone_field, CREDENTIALS["LOGIN"])
        self.input_text(elements.FIELDS["PASSWORD_ID"], CREDENTIALS["PASSWORD"])

        # Save password in app
        keepPasswordCheckbox = self.get_element_with_wait(
            elements.CHECKBOXES["KEEP_PASSWORD_ID"]
        )
        isChecked = str2bool(keepPasswordCheckbox.get_attribute("checked"))
        if not isChecked:
            keepPasswordCheckbox.click()

        # Click login button
        self.get_element_with_wait(elements.BUTTONS["LOGIN_ID"]).click()

    def get_element_with_wait(self, value, timeout=0, type='ID'):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((getattr(By, type), value)))
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def input_text(self, where, text, type='ID'):
        if (isinstance(where, WebElement)):
            where.send_keys(text)
        else:
            self.get_element_with_wait(type=type, value=where).send_keys(text)


if __name__ == '__main__':
    app = AutobonusDriver()
    app.setUp()

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from time import sleep
import elements
def str2bool(str):
    if (str == 'true'):
        return True
    elif (str == 'false'):
        return False
    else:
        raise TypeError(f'Cannot convert string with value "{str}" to bool')


class ChessAndroidTests():

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = '/home/antiss/Downloads/life.apk'
        desired_caps['appium:appWaitForLaunch'] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)
        sleep(10)
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
        self.inputText(phone_field, CREDENTIALS['LOGIN'])
        self.inputText(
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

    def inputText(self, where, type, text):
        # print(isinstance(where, WebElement))
        if (isinstance(where, WebElement)):
            where.send_keys(text)
        else:
            self.get_element(type=type, value=where).send_keys(text)


if __name__ == '__main__':
    app = ChessAndroidTests()
    app.setUp()

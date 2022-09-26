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


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = '/home/antiss/Downloads/life.apk'
        desired_caps['appium:appWaitForLaunch'] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)
        sleep(10)
        self.driver.find_element(
            by=AppiumBy.ID, value=elements.BUTTONS['NOTIFICATIONS_DENY']).click()
        sleep(4)
        if self.loginNeeded:
            self.inputText(elements.FIELDS['PHONE'], NUMBER)
            self.inputText(elements.FIELDS['PASSWORD'], PASSWORD)
            sleep(2)
            keepPasswordCheckbox = self.driver.find_element(
                by=AppiumBy.ID, value=elements.CHECKBOXES['KEEP_PASSWORD'])
            print(keepPasswordCheckbox.get_attribute('checked'))

    def loginNeeded(self):
        phoneField = self.driver.find_element(
            by=AppiumBy.ID, value=elements.FIELDS['PHONE'])
        if phoneField:
            return True
        else:
            return False

    def inputText(self, where, text):
        self.driver.find_element(by=AppiumBy.ID, value=where).send_keys(text)


if __name__ == '__main__':
    app = ChessAndroidTests()
    app.setUp()

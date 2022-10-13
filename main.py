from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.webelement import WebElement
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import elements
import subprocess
import yaml
from typing import Type
from os.path import abspath


def str2bool(str: str) -> bool | None:
    if str == "true":
        return True
    elif str == "false":
        return False
    else:
        raise TypeError(f'Cannot convert string with value "{str}" to bool')


class AutobonusDriver:
    def __init__(self):
        with open("config.yml", "r") as stream:
            self.config = yaml.safe_load(stream)

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "Android Emulator"
        apk_path = self.config["apk_path"]
        if apk_path:
            desired_caps["app"] = apk_path
        else:
            desired_caps["app"] = abspath("life.apk")
        desired_caps["appium:appWaitForLaunch"] = False
        url = (
            f"http://{self.config['appium_server']['host']}:"
            f"{self.config['appium_server']['port']}/wd/hub"
        )
        self.driver = webdriver.Remote(url, desired_caps)

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

        self.input_text(phone_field, self.config["credentials"]["login"])
        self.input_text(
            elements.FIELDS["PASSWORD_ID"], self.config["credentials"]["password"]
        )

        # Save password in app
        keepPasswordCheckbox = self.get_element_with_wait(
            elements.CHECKBOXES["KEEP_PASSWORD_ID"]
        )
        isChecked = str2bool(keepPasswordCheckbox.get_attribute("checked"))
        if not isChecked:
            keepPasswordCheckbox.click()

        # Click login button
        self.get_element_with_wait(elements.BUTTONS["LOGIN_ID"]).click()

    def skip_protection(self):
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

    def select_game(self):
        self.get_element_with_wait(elements.BUTTONS["MENU_ID"], timeout=20).click()
        self.get_element_with_wait(elements.BUTTONS["GAME_ID"], timeout=10).click()

    def take_bonus(self):
        self.get_element_with_wait(elements.GAME["PONY_ID"], timeout=30)
        subprocess.run(
            (
                f"./shake.sh {self.config['emulator']['host']} "
                f"{self.config['emulator']['port']} {self.config['telnet_token']}"
            ),
            shell=True,
        )

    def get_element_with_wait(
        self, value: str, timeout: int | float = 0, type: str = "ID"
    ):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((getattr(By, type), value))
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def input_text(self, where: str | Type[WebElement], text: str, type: str = "ID"):
        if isinstance(where, WebElement):
            where.send_keys(text)
        else:
            self.get_element_with_wait(type=type, value=where).send_keys(text)


if __name__ == "__main__":
    app = AutobonusDriver()

    app.setUp()
    app.login()
    app.skip_protection()
    app.select_game()
    app.take_bonus()

import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage(TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get("https://buyme.co.il/")

    def click_sign_in_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "li.notSigned[data-ember-action='1012']").click()


class LoggedInHomePage(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def assert_logged_in_home_page(self):
        assert self.driver.find_element(By.ID, "ember1921")


driver = webdriver.Chrome(executable_path="C:\\path\\to\\chrome-win32\\chrome-win32\\chrome.exe")

home_page = Homepage(driver)
home_page.go_to_home_page()
home_page.click_sign_in_button()
logged_in_home_page = LoggedInHomePage(driver)
logged_in_home_page.assert_logged_in_home_page()
driver.quit()

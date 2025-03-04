# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.service import Service

class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="C:\Windows\SysWOW64\geckodriver.exe")
        self.driver = webdriver.Firefox(service=service)
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/addressbook/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

        # Логин
        self.login("admin", "secret")
        # Создание группы
        group = Group("lozka", "kolbasa", "spati")
        self.create_new_group(group)
        # Логаут
        self.logout()

    def login(self, username, password):
         self.open_home_page()
         self.fill_login_form(username, password)
         self.submit_login()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def fill_login_form(self, username, password):
        driver = self.driver
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").clear()
        self.driver.find_element(By.NAME, "pass").send_keys(password)

    def submit_login(self):
        driver = self.driver
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def create_new_group(self, group):
        driver = self.driver
        self.open_groups_page()
        self.init_group_creation()
        self.fill_group_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()
    def open_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def init_group_creation(self):
        driver = self.driver
        driver.find_element(By.NAME, "new").click()

    def fill_group_form(self, group):
        driver = self.driver
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def submit_group_creation(self):
        driver = self.driver
        driver.find_element(By.NAME, "submit").click()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
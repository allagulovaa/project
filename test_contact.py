# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.service import Service


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
        driver.get("http://localhost/addressbook/edit.php")
        self.login("admin", "secret")
        self.create_contact(
            "Alina",
            "Mitrofanova",
            "painkiller",
            "ergr",
            "rgreg",
            "hty",
            "weew",
            "34343546",
            "ffeewe",
            "nyjt4",
            "egrhtjkjythrew@GRGR.RU",
            "14",
            "July",
            "2001",
        )
        self.return_to_home_page()

    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def create_contact(
        self,
        firstname,
        middlename,
        nickname,
        title,
        company,
        address,
        homephone,
        mobilephone,
        workphone,
        fax,
        email,
        bday,
        bmonth,
        byear,
    ):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "add new").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(firstname)
        driver.find_element(By.NAME, "middlename").clear()
        driver.find_element(By.NAME, "middlename").send_keys(middlename)
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys(nickname)
        driver.find_element(By.NAME, "title").clear()
        driver.find_element(By.NAME, "title").send_keys(title)
        driver.find_element(By.NAME, "company").clear()
        driver.find_element(By.NAME, "company").send_keys(company)
        driver.find_element(By.NAME, "address").clear()
        driver.find_element(By.NAME, "address").send_keys(address)
        driver.find_element(By.NAME, "home").clear()
        driver.find_element(By.NAME, "home").send_keys(homephone)
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys(mobilephone)
        driver.find_element(By.NAME, "work").clear()
        driver.find_element(By.NAME, "work").send_keys(workphone)
        driver.find_element(By.NAME, "fax").clear()
        driver.find_element(By.NAME, "fax").send_keys(fax)
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys(email)
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text(bday)
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text(bmonth)
        driver.find_element(By.NAME, "byear").clear()
        driver.find_element(By.NAME, "byear").send_keys(byear)
        driver.find_element(By.XPATH, "//input[@value='Enter']").click()

    def return_to_home_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
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
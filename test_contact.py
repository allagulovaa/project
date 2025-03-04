# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class SessionHelper:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.open_home_page()
        self.fill_login_form(username, password)
        self.submit_login()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def fill_login_form(self, username, password):
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").clear()
        self.driver.find_element(By.NAME, "pass").send_keys(password)

    def submit_login(self):
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

class GroupHelper:
    def __init__(self, driver):
        self.driver = driver

    def create_group(self, group):
        self.open_groups_page()
        self.init_group_creation()
        self.fill_group_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def init_group_creation(self):
        self.driver.find_element(By.NAME, "new").click()

    def fill_group_form(self, group):
        self.driver.find_element(By.NAME, "group_name").clear()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").clear()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").clear()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def submit_group_creation(self):
        self.driver.find_element(By.NAME, "submit").click()

    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def is_group_created(self, group_name):
        self.open_groups_page()
        try:
            self.driver.find_element(By.XPATH, f"//span[text()='{group_name}']")
            return True
        except NoSuchElementException:
            return False

class ContactHelper:
    def __init__(self, driver):
        self.driver = driver

    def create_contact(self, contact):
        pass

    def edit_contact(self, contact):
        pass

    def delete_contact(self):
        pass

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.session = SessionHelper(self.driver)
        self.group = GroupHelper(self.driver)
        self.contact = ContactHelper(self.driver)

@pytest.fixture(scope="module")
def app():
    service = Service(executable_path="C:\\Windows\\SysWOW64\\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    app = Application(driver)
    yield app
    driver.quit()

@pytest.fixture
def test_group():
    return Group(name="lozka", header="kolbasa", footer="spati")

def test_create_group(app, test_group):
    app.session.login("admin", "secret")
    app.group.create_group(test_group)
    assert app.group.is_group_created(test_group.name), "Группа не была создана"
    app.session.logout()

def test_create_contact(app):
    app.session.login("admin", "secret")
    app.session.logout()
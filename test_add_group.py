# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.firefox.service import Service

class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path="C:\Windows\SysWOW64\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    def _login(username, password):
        open_home_page(driver)
        fill_login_form(driver, username, password)
        submit_login(driver)
    return _login

@pytest.fixture
def logout(driver):
    def _logout():
        driver.find_element(By.LINK_TEXT, "Logout").click()
    return _logout

@pytest.fixture
def create_group(driver):
    def _create_group(group):
        open_groups_page(driver)
        init_group_creation(driver)
        fill_group_form(driver, group)
        submit_group_creation(driver)
        return_to_groups_page(driver)
    return _create_group

def open_home_page(driver):
    driver.get("http://localhost/addressbook/")

def fill_login_form(driver, username, password):
    driver.find_element(By.NAME, "user").clear()
    driver.find_element(By.NAME, "user").send_keys(username)
    driver.find_element(By.NAME, "pass").clear()
    driver.find_element(By.NAME, "pass").send_keys(password)

def submit_login(driver):
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

def open_groups_page(driver):
    driver.find_element(By.LINK_TEXT, "groups").click()

def init_group_creation(driver):
    driver.find_element(By.NAME, "new").click()

def fill_group_form(driver, group):
    driver.find_element(By.NAME, "group_name").clear()
    driver.find_element(By.NAME, "group_name").send_keys(group.name)
    driver.find_element(By.NAME, "group_header").clear()
    driver.find_element(By.NAME, "group_header").send_keys(group.header)
    driver.find_element(By.NAME, "group_footer").clear()
    driver.find_element(By.NAME, "group_footer").send_keys(group.footer)

def submit_group_creation(driver):
    driver.find_element(By.NAME, "submit").click()

def return_to_groups_page(driver):
    driver.find_element(By.LINK_TEXT, "group page").click()

def test_create_group(driver, login, logout, create_group):
    driver.get("http://localhost/addressbook/")
    login("admin", "secret")
    group = Group("lozka", "kolbasa", "spati")
    create_group(group)
    logout()
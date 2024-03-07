from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import os

link = "https://testpages.eviltester.com/styled/index.html"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

class TestStringMethods():
    def test_one(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[contains(text(),'HTML5 Element Form Test Page')]").click()
        browser.find_element(By.ID, "colour-picker").send_keys("#000000")
        browser.find_element(By.ID, "date-picker").send_keys("2002-02-02")
        browser.find_element(By.ID, "date-time-picker").send_keys("2002-02-02T02:02")
        browser.find_element(By.ID, "email-field").clear()
        browser.find_element(By.ID, "email-field").send_keys("bob@mailinator.com")
        browser.find_element(By.ID, "month-field").send_keys(Keys.ARROW_UP, Keys.TAB, Keys.ARROW_UP)
        browser.find_element(By.ID, "number-field").clear()
        browser.find_element(By.ID, "number-field").send_keys("42")
        browser.find_element(By.NAME, "submitbutton").click()
        assert browser.find_element(By.XPATH, "//li[@id='_valuecolour'][contains(text(),'000000')]").is_displayed()
        assert browser.find_element(By.XPATH, "//li[@id='_valuedate'][contains(text(),'2002-02-02')]").is_displayed()
        assert browser.find_element(By.XPATH, "//li[@id='_valuedatetime'][contains(text(),'2002-02-02T02:02')]").is_displayed()
        assert browser.find_element(By.XPATH, "//li[@id='_valueemail'][contains(text(),'bob@mailinator.com')]").is_displayed()
        assert browser.find_element(By.XPATH, "//li[@id='_valuemonth'][contains(text(),'2024-01')]").is_displayed()
        assert browser.find_element(By.XPATH, "//li[@id='_valuenumber'][contains(text(),'42')]").is_displayed()

    def test_two(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "basicauth").click()
        usernameEl = browser.find_element(By.XPATH, "//p[contains(text(),'username')]")
        username = usernameEl[10:]
        passwordEl = browser.find_element(By.XPATH, "//p[contains(text(),'password')]")
        password = usernameEl[10:]
        browser.find_element(By.XPATH, "//a[contains(text(),'Basic Auth Protected Page')]").click()
        assert browser.find_element(By.ID, "status") == "Authenticated"

    def test_three(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "fileuploadtest").click()
        browser.find_element(By.ID, "itsafile").click()
        file = open(os.getcwd() + "\\" + 'test' + '.txt', 'rb')
        browser.find_element(By.ID, "fileinput").send_keys(file)
        browser.find_element(By.NAME, "upload").click()
        assert browser.find_element(By.XPATH, "//p[contains(text(),'You uploaded a file. This is the result')]").is_displayed()

    def test_four(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "alerttestjs").click()
        browser.find_element(By.ID, "alertexamples").click()
        Alert(browser).accept()
        assert browser.find_element(By.XPATH, "//p[contains(text(),'You triggered and handled the alert dialog')]").is_displayed()
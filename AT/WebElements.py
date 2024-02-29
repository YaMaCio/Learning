from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os

link = "https://testpages.eviltester.com/styled/index.html"
browser = driver = webdriver.Chrome()

@pytest.fixture
def setting():
    browser = driver = webdriver.Chrome()
    browser.implicitly_wait(10)

class TestStringMethods():
    def test_one(self):
        setting()
        browser.get(link)
        driver.find_element(By.XPATH, "//a[contains(text(),'HTML5 Element Form Test Page')]").click()
        driver.find_element(By.ID, "colour-picker").send_keys("#000000")
        driver.find_element(By.ID, "date-picker").send_keys("2002-02-02")
        driver.find_element(By.ID, "date-time-picker").send_keys("2002-02-02T02:02")
        driver.find_element(By.ID, "email-field").clear()
        driver.find_element(By.ID, "email-field").send_keys("bob@mailinator.com")
        driver.find_element(By.ID, "month-field").send_keys("2002-02")
        driver.find_element(By.ID, "number-field").send_keys("42")
        driver.find_element(By.NAME, "submitbutton").click()
        assert driver.find_element(By.ID, "_valuecolour") == "#000000"
        assert driver.find_element(By.ID, "_valuedate") == "2002-02-02"
        assert driver.find_element(By.ID, "_valuedatetime") == "2002-02-02T02:02"
        assert driver.find_element(By.ID, "_valueemail") == "bob@mailinator.com"
        assert driver.find_element(By.ID, "_valuemonth") == "2002-02"
        assert driver.find_element(By.ID, "_valuenumber") == "42"
        browser.quit()

    def test_two(self):
        setting()
        browser.get(link)
        driver.find_element(By.ID, "basicauth").click()
        usernameEl = driver.find_element(By.XPATH, "//p[contains(text(),'username')]")
        username = usernameEl[10:]
        passwordEl = driver.find_element(By.XPATH, "//p[contains(text(),'password')]")
        password = usernameEl[10:]
        driver.find_element(By.XPATH, "//a[contains(text(),'Basic Auth Protected Page')]").click()
        assert driver.find_element(By.ID, "status") == "Authenticated"
        browser.quit()

    def test_three(self):
        setting()
        browser.get(link)
        driver.find_element(By.ID, "fileuploadtest").click()
        driver.find_element(By.ID, "itsafile").click()
        file = open(os.getcwd() + 'test' + '.txt', 'rb')
        driver.find_element(By.ID, "fileinput").send_keys(file)
        driver.find_element(By.NAME, "upload").click()
        assert driver.find_element(By.XPATH, "//p[contains(text(),'You uploaded a file. This is the result')]").is_displayed()
        browser.quit()

    def test_four(self):
        setting()
        browser.get(link)
        driver.find_element(By.ID, "alerttestjs").click()
        driver.find_element(By.ID, "alertexamples").click()
        Alert(driver).accept()
        assert driver.find_element(By.XPATH, "//p[contains(text(),'You triggered and handled the alert dialog')]").is_displayed()
        browser.quit()
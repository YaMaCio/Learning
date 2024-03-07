from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
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
        browser.find_element(By.ID, "button01").click()
        browser.find_element(By.ID, "button00").click()
        browser.find_element(By.ID, "button01").click()
        time.sleep(5)
        assert browser.find_element(By.ID, "button02").is_enabled()

    def test_two(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "button01").click()
        browser.find_element(By.ID, "button00").click()
        browser.find_element(By.ID, "button01").click()
        assert browser.find_element(By.ID, "button02").is_enabled()

    def test_three(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "button01").click()
        browser.find_element(By.ID, "button00").click()
        browser.find_element(By.ID, "button01").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.ID, "button02"))
        assert browser.find_element(By.ID, "button02").is_enabled()
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=20"
browser = driver = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)
driver.find_element(By.XPATH, "//a[contains(text(),'Tablets')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Samsung Galaxy Tab 10.1')]").click()
assert driver.find_element(By.XPATH, "//p[contains(text(),'720p HD video recording capability')]").is_displayed()
browser.quit()
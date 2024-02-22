from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://chmnu.edu.ua/"
    #Налаштуваня веб-драйверу на браузер Chrome
    browser = webdriver.Chrome()
    #Відправка HTTP GET запросу за вказаним URL
    browser.get(link)
    #Пошук елемента DOM-дерева по ID
    button = browser.find_element(By.ID, "s")
    #Клік на знайдений елемент
    button.click()
   
finally:
    #Завершення роботи
    browser.quit()
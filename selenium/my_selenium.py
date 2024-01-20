import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.daraz.pk/")
data = driver.find_element(By.NAME, "q")
data.send_keys("mouse for pc")
btn = driver.find_element(By.XPATH, "//button[@class='search-box__button--1oH7']")
btn.click()
item = driver.find_elements(By.ID, "id-a-link")
for i in item:
    lk = i.get_attribute("href")
    link.append(lk)
time.sleep(4)
for i  in link:
    print(i)
print(len(link))

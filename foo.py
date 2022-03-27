import http.client
import socket
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.nycu.edu.tw/news-network/')
element = driver.find_element(By.ID, '-tab')
lis = element.find_elements(By.TAG_NAME, 'li')
lis[0].find_element(By.TAG_NAME, 'a').click()
print(driver.current_url)
driver.quit()

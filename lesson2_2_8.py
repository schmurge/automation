from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '123.txt')

browser = webdriver.Chrome()
browser. get('https://suninjuly.github.io/file_input.html')

browser.find_element(By.NAME, 'firstname').send_keys('test')
browser.find_element(By.NAME, 'lastname').send_keys('test')
browser.find_element(By.NAME, 'email').send_keys('test@text.cds')

file = browser.find_element(By.ID, 'file')
file.send_keys(file_path)

browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(30)
browser.quit()
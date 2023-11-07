from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/get_attribute.html')

treasure = browser.find_element(By.ID, 'treasure')
x = treasure.get_attribute('valuex')

result = math.log(abs(12*math.sin(int(x))))

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(result)

robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
robotCheckbox.click()
robotRadio = browser.find_element(By.ID, 'robotsRule')
robotRadio.click()
button = browser.find_element(By.TAG_NAME, 'button')
button.click()

time.sleep(20)

browser.quit()
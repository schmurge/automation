from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, 'input_value').text
result = str(math.log(abs(12*math.sin(int(x)))))

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(result)

robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
robotCheckbox.click()

robotsRuleRadio = browser.find_element(By.ID, 'robotsRule')
robotsRuleRadio.click()

submitButton = browser.find_element(By.TAG_NAME, 'button')
submitButton.click()

time.sleep(10)
browser.quit()
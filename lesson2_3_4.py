from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/alert_accept.html')

browser.find_element(By.CLASS_NAME, 'btn-primary').click()

browser.switch_to.alert.accept()

x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.NAME, 'text').send_keys(math.log(abs(12*math.sin(x))))

browser.find_element(By.CLASS_NAME, 'btn').click()

result = browser.switch_to.alert.text
print(result.split(': ')[1])

time.sleep(10)
browser.quit()
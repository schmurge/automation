from selenium.webdriver.common.by import By
from selenium import webdriver
import math, time

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/redirect_accept.html')

browser.find_element(By.CLASS_NAME, 'btn').click()

browser.switch_to.window(browser.window_handles[1])

result = math.log(abs(12*math.sin(int(browser.find_element(By.ID, 'input_value').text))))
browser.find_element(By.ID, 'answer').send_keys(result)

browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

print(browser.switch_to.alert.text.split(': ')[1])

time.sleep(10)
browser.quit()
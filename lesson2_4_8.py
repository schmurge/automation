from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import math


browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

browser.find_element(By.ID, 'book').click()

result = math.log(abs(12*math.sin(int(browser.find_element(By.ID, 'input_value').text))))
browser.find_element(By.ID, 'answer').send_keys(result)
browser.find_element(By.ID, 'solve').click()

print(browser.switch_to.alert.text.split(': ')[1])

browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

result = math.log(abs(12*math.sin(int(str(browser.find_element(By.ID, 'input_value').text)))))
browser.find_element(By.ID, 'answer').send_keys(result)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()

button.click()


time.sleep(100)
browser.quit()
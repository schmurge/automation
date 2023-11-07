from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects2.html')

browser.execute_script("document.title='Script executing';alert('Robots at work');")
# dropdown = Select(browser.find_element(By.ID, 'dropdown'))
# dropdown.select_by_visible_text(str(int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)))
#
# browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(10)
browser.quit()
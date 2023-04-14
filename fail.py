import math
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# browser = webdriver.Chrome()
# browser.get('https://suninjuly.github.io/selects1.html')
#
# x = browser.find_element(By.XPATH, '//span[@id="num1"]')
# y = browser.find_element(By.XPATH, '//span[@id="num2"]')
# s = int(x.text) + int(y.text)
# select = Select(browser.find_element(By.XPATH, '//select[@class="custom-select"]'))
# select.select_by_value(str(s))
#Скрол:
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/execute_script.html')
# x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
# x = x_element.text
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
#
# rules_element = browser.find_element(By.XPATH, '//input[@id="answer"]')
# rules_element.send_keys(calc(int(x)))
#Добавления файла:
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/file_input.html')
#
# firstname = browser.find_element(By.XPATH, '//input[@name="firstname"]')
# firstname.send_keys('Edgar')
# lastname = browser.find_element(By.XPATH, '//input[@name="lastname"]')
# lastname.send_keys('Fanyan')
# email = browser.find_element(By.XPATH, '//input[@name="email"]')
# email.send_keys('edgar@mail.ru')
# file = browser.find_element(By.XPATH, '//input[@name="file"]')
# current_dir = os.path.abspath(os.path.dirname('C:\Новый текстовый документ.txt'))
# file_path = os.path.join(current_dir, 'C:\Новый текстовый документ.txt')
# file.send_keys(file_path)
# submit = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
# submit.click()

# alert:
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/alert_accept.html')
#
# jour = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
# jour.click()
# confrim = browser.switch_to.alert
# confrim.accept()
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# Новая ссылка :
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/redirect_accept.html')
#
# new = browser.find_element(By.XPATH, '//button[@class="trollface btn btn-primary"]')
# new.click()
# new_window = browser.window_handles[1]
# browser._switch_to.window(new_window)
# wsw = browser.find_element(By.XPATH, '//input[@class="form-control"]')
# wsw.send_keys('TEMBOT LOX')
# time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


browser.get('http://suninjuly.github.io/explicit_wait2.html')
call = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element([By.XPATH, '//h5[@id="price"]'], "100"))
book = browser.find_element(By.XPATH, '//button[@id="book"]')
book.click()


time.sleep(10)
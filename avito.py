import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/get_attribute.html')

# x_element = driver.find_element(By.XPATH, '//span[@id="input_value"]')
# x = x_element.text

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# rules_element = driver.find_element(By.XPATH, '//input[@id="answer"]')
# rules_element.send_keys(int(calc(x)))

# checkbox_element = driver.find_element(By.XPATH,'//input[@id="robotCheckbox"]')
# checkbox_element.click()
# radiobutton_element = driver.find_element(By.XPATH,'//input[@id="robotsRule"]')
# radiobutton_element.click()
# submit_element = driver.find_element(By.XPATH, '//button[@class="btn btn-default"]')
# submit_element.click()

# people_radio = driver.find_element(By.ID, "peopleRule")
# people_checked = people_radio.get_attribute("checked")
# print("value of people radio: ", people_checked)
# assert people_checked == "true", "People radio is not selected by default"

# x_element = driver.find_element(By.XPATH, '//img[@id="treasure"]')
# x = x_element.get_attribute("valuex")
# rules_element = driver.find_element(By.XPATH, '//input[@id="answer"]')
# rules_element.send_keys(x)
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# checkbox_element = driver.find_element(By.XPATH,'//input[@id="robotCheckbox"]')
# checkbox_element.click()
# radiobutton_element = driver.find_element(By.XPATH,'//input[@id="robotsRule"]')
# radiobutton_element.click()
# submit_element = driver.find_element(By.XPATH, '//button[@class="btn btn-default"]')
# submit_element.click()


time.sleep(10)


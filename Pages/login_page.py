import time

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from webdriver_manager import driver

@when(parsers.cfparse("User enter mobile number '{number}' and password '{password}'"))
def login_details(driver,number, password):
  var = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
  var.send_keys(number)
  var1 = driver.find_element(By.XPATH, "//input[@class='_2IX_2- _3mctLh VJZDxU']")
  var1.send_keys(password)
  submit = driver.find_element(By.XPATH,  "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
  submit.click()


time.sleep(5)
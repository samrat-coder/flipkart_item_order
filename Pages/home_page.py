import time

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from webdriver_manager import driver

@when(parsers.cfparse("User search item '{mobiles}'"))
def search_item(driver, mobiles):
 time.sleep(5)
 search = driver.find_element(By.XPATH, "//input[@name='q']")
 # search.click()
 search.send_keys(mobiles)
 submit = driver.find_element(By.XPATH, "//button[@type='submit']")
 submit.click()


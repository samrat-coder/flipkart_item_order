import time

from pytest_bdd import when
from selenium.webdriver.common.by import By

@when("User select delevery")
def delevery(driver):
    time.sleep(5)
    address = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l RLM7ES _3AWRsL']")
    address.click()

@when("User select continue")
def contiue(driver):
    time.sleep(5)
    order = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _1seccl _3AWRsL']")
    order.click()
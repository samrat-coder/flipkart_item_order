import time

from pytest_bdd import when
from selenium.webdriver.common.by import By
from webdriver_manager import driver

@when("User select buy now")
def buy_ittem(driver):
 buy = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']")
 buy.click()

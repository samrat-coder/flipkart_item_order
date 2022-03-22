import time

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@when("User select credit card")
def card_select(driver):
    time.sleep(10)
    method = driver.find_element(By.XPATH, "//label[@for='CREDIT']")
    method.click()

@when(parsers.cfparse("User enter credit card number '{card_number}'"))
def card_number(driver, card_number):
    time.sleep(5)
    card = driver.find_element(By.XPATH, "//input[@name='cardNumber']")
    card.click()
    card.send_keys(card_number)

@when(parsers.cfparse("User enter month '{month_number}'"))
def select_month(driver, month_number):
    time.sleep(5)
    month = driver.find_element(By.XPATH, "//select[@name='month']")
    number = Select(month)
    number.select_by_value(month_number)

@when(parsers.cfparse("User enter year '{year_number}'"))
def select_year(driver, year_number):
    time.sleep(5)
    year = driver.find_element(By.XPATH, "//select[@name='year']")
    number = Select(year)
    number.select_by_value(year_number)

@when(parsers.cfparse("User enter cvv '{cvv_pin}'"))
def select_cvv(driver, cvv_pin):
    time.sleep(5)
    cvv = driver.find_element(By.XPATH, "//input[@name='cvv']")
    cvv.click()
    cvv.send_keys(cvv_pin)

@when("User select pay amount")
def pay_ammount(driver):
    time.sleep(5)
    pay = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2hNkcG _2nejCf _3AWRsL']")
    pay.click()



import time
from select import select

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@when(parsers.cfparse("User short price '{price_value}'"))
def sort_price(driver, price_value):
    time.sleep(5)
    var3 = driver.find_element(By.XPATH, "//div[@class='_3uDYxP']/select")
    drop = Select(var3)
    drop.select_by_value(price_value)

@when(parsers.cfparse("User select brand name '{realme}'"))
def brand_name(driver,realme):
    time.sleep(5)
    var2 = driver.find_element(By.XPATH, "//input[@placeholder='Search Brand']")
    var2.send_keys(realme)
    brand = driver.find_element(By.XPATH, "//div[@title='realme']")
    brand.click()
@when("User select first item")
def select_item(driver):
    time.sleep(5)
    item = driver.find_element(By.XPATH, "//div[text()='realme C11 2021 (Cool Blue, 32 GB)']")
    item.click()

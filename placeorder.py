from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

def close_last_tab():
    if (len(driver.window_handles) == 2):
        driver.switch_to.window(window_name=driver.window_handles[0])
        driver.close()
        driver.switch_to.window(window_name=driver.window_handles[-1])

test_username = input("Enter your snapdeal username: ")
test_password = input("Enter you snapdeal password: ")
test_search = input("Enter name of product you want to search: ")

# Load webdriver 
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

# Access URL
driver.get("https://www.snapdeal.com/login")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

# Enter email name and check user
email_field = driver.find_element_by_id("userName")
email_field.send_keys(test_username)
driver.find_element_by_id("checkUser").click()

# Enter password and login
wait = WebDriverWait(driver, 10)
password_field = wait.until(EC.element_to_be_clickable((By.ID,'j_password_login_uc')))
password_field.send_keys(test_password)
driver.find_element_by_id("submitLoginUC").click()

# Search product
search_field = wait.until(EC.element_to_be_clickable((By.ID,'inputValEnter')))
search_field.send_keys(test_search)
driver.find_element_by_class_name("searchformButton").click()

# Open first product page
products = wait.until(EC.element_to_be_clickable((By.ID,'products')))
product = products.find_element_by_class_name("product-tuple-listing")
product.click()

close_last_tab()
add_cart = wait.until(EC.element_to_be_clickable((By.ID,'add-cart-button-id')))
add_cart.click()

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

URL = 'https://automationexercise.com'

driver.get(URL)

act_title = driver.title
homepage_title = "Automation Exercise"

if act_title == homepage_title:
    print("Home Page is visible")
else: 
    print("Home Page is not visible")

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a").click()

driver.refresh()

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a").click()

add_cart1 = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]")

hover_cart = ActionChains(driver).move_to_element(add_cart1)

hover_cart.perform()

driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/a").click()

# CLick modal

modal_continue = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cartModal']/div/div/div[3]/button")))

modal_continue.click()

add_cart2 = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[2]")

hover_cart = ActionChains(driver).move_to_element(add_cart2)

hover_cart.perform()

driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div/a").click()

modal_view_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")))

modal_view_cart.click()

# Print semua product

cart_products = driver.find_elements(By.CLASS_NAME, "cart_product")
print(len(cart_products))

if len(cart_products) == 2:
    print("Both products are added")
else:
    print("Both products are not added")

cart_info = driver.find_element(By.ID, "product-1")
details_cart_info = cart_info.find_elements(By.TAG_NAME, 'td')

for detail in details_cart_info:
    print(detail.text)

cart_info = driver.find_element(By.ID, "product-2")
details_cart_info = cart_info.find_elements(By.TAG_NAME, 'td')

for detail in details_cart_info:
    print(detail.text)

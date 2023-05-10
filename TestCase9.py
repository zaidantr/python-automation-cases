from selenium import webdriver
import time as time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

URL = 'https://automationexercise.com/'

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

act_title = driver.title
products_title = f"{homepage_title} - All Products"

if act_title == products_title:
    print("All products is visible")
else: 
    print("All products is not visible")

item = 'Blue Top'

driver.find_element(By.ID, "search_product").send_keys(item)
driver.find_element(By.ID, "submit_search").click()

act_title = driver.find_element(By.CLASS_NAME, "title")
print("SEARCHED PRODUCTS is visibile: ", act_title.is_displayed())

product_info = driver.find_element(By.CLASS_NAME, "productinfo")
product_name = product_info.find_element(By.TAG_NAME, 'p').text

if item == product_name:
    print("Product is related")
else:
    print("Product is not related")
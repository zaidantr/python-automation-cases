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

driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/ul/li/a").click()

product_details = driver.find_element(By.CLASS_NAME, "product-details")
product_name = product_details.find_element(By.TAG_NAME, 'h2').text

print(product_name)
others = product_details.find_elements(By.TAG_NAME, "p")

for other in others:
    print(other.text)
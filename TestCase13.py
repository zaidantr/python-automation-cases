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

driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a").click()

driver.refresh()

driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a").click()

quantity = "4"
driver.find_element(By.ID, "quantity").clear()
driver.find_element(By.ID, "quantity").send_keys(quantity)

driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button").click()

modal_continue = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")))

modal_continue.click()

# Print semua product

cart_info = driver.find_element(By.ID, "product-1")
details_cart_info = cart_info.find_elements(By.TAG_NAME, 'td')

for detail in details_cart_info:
    if detail.text == quantity:
        print("Jumlah sama")
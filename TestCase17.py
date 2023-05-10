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

add_cart1 = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]")
driver.execute_script("arguments[0].scrollIntoView();", add_cart1)

hover_cart = ActionChains(driver).move_to_element(add_cart1)

hover_cart.perform()

driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a").click()

modal_continue = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")))

modal_continue.click()

cart_page = driver.find_element(By.XPATH, "//*[@id='cart_items']/div/div[1]/ol/li[2]")

print("Cart page is visible: ", cart_page.is_displayed())

driver.find_element(By.CLASS_NAME, "cart_quantity_delete").click()

driver.refresh()

cart_empty = driver.find_element(By.CLASS_NAME, "text-center")
print(cart_empty)

if cart_empty.is_displayed():
    print("Product is removed")
else:
    print("Product is exist")
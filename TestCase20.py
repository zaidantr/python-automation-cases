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
    print("'SEARCHED PRODUCTS' is visibile")
else:
    print("'SEARCHED PRODUCTS' is not visible")

view = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
driver.execute_script("arguments[0].scrollIntoView();", view)

hover_cart = ActionChains(driver).move_to_element(view)

hover_cart.perform()

driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a").click()

modal_view = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")))

modal_view.click()

product_cart = driver.find_element(By.XPATH, "//*[@id='product-1']/td[2]/h4/a").text

if product_cart == item:
    print("PRODUCTS is visible")
else:
    print("PRODUCTS is not visibile")

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a").click()

email = "butokbuton@gmail.com"
password = "432zenius"

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]").send_keys(email)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]").send_keys(password)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button").click()

# driver.refresh()

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a").click()

product_cart = driver.find_element(By.XPATH, "//*[@id='product-1']/td[2]/h4/a").text

if product_cart == item:
    print("PRODUCTS is visible after login")
else:
    print("PRODUCTS is not visibile after login after login")

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

recommended = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[2]/h2")
driver.execute_script("arguments[0].scrollIntoView();", recommended)

if recommended.is_displayed():
    print("'RECOMMENDED ITEMS' are visible")
else: 
    print("'RECOMMENDED ITEMS' are not visible")

driver.find_element(By.XPATH, "//*[@id='recommended-item-carousel']/div/div[2]/div[1]/div/div/div/a").click()

modal_view = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[2]/a")))

modal_view.click()

product_cart = driver.find_element(By.XPATH, "//*[@id='product-4']/td[2]/h4/a")

if product_cart.is_displayed():
    print("PRODUCTS is visible")
else:
    print("PRODUCTS is not visibile")

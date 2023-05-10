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
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@href='/products']").click()

driver.refresh()

driver.find_element(By.XPATH, "//a[@href='/products']").click()

category_section = driver.find_element(By.CLASS_NAME, "left-sidebar")

driver.execute_script("arguments[0].scrollIntoView();", category_section)
if category_section.is_displayed():
    print("Categories are visible on left side bar")
else:
    print("Categories are NOT visible on left side bar")

driver.find_element(By.XPATH, "//a[@href='/brand_products/Polo']").click()

brand_polo = driver.find_element(By.XPATH, "(//h2[normalize-space()='Brand - Polo Products'])[1]")

if brand_polo.is_displayed():
    print("Brand POLO products are displayed is true")
else:
    print("Brand POLO products are displayed is false")

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[1]/div/div[2]/div/ul/li[2]/a").click()

driver.refresh()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[1]/div/div[2]/div/ul/li[2]/a").click()

brand_hm = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[2]/div/h2")

if brand_hm.is_displayed():
    print("Brand HM products are displayed is true")
else:
    print("Brand HM products are displayed is false")
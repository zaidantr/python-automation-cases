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

view = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a")
driver.execute_script("arguments[0].scrollIntoView();", view)

view.click()

name = "Butok Buton"
email = "butokbuton@gmail.com"
review = "Hehe"

name_input = driver.find_element(By.ID, "name")
driver.execute_script("arguments[0].scrollIntoView();", name_input)
name_input.send_keys(name)

driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "review").send_keys(review)
driver.find_element(By.ID, "review").send_keys(review)

time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

driver.find_element(By.ID, "button-review").click()

time.sleep(1)
ty_msg = driver.find_element(By.ID, "review-section")

if ty_msg.is_displayed():
    print("Thank you is visible")
else: 
    print("Thank you is not visible")
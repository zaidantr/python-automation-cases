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

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a").click()

act_title = driver.title
sign_title = f"{homepage_title} - Signup / Login"

if act_title == sign_title:
    print("Sign up is visible")
else: 
    print("Sign up is not visible")

name = "Buton Buton"
email = "butokbuton@gmail.com"

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[2]").send_keys(name)
driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]").send_keys(email)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button").click()

act_title = driver.title
signup_title = f"{homepage_title} - Signup"

if act_title == signup_title:
    print("Email Address is not already exist!")
else: 
    err_msg = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/p")
    print("Email Address already exist! is:", err_msg.is_displayed())


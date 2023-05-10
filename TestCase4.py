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

email = "butokbuton@gmail.com"
password = "432zenius"

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]").send_keys(email)
driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]").send_keys(password)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button").click()

# Verify
login_msg = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")

print("Logged in as username is:", login_msg.is_displayed())

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a").click()

act_title = driver.title
signup_title = f"{homepage_title} - Signup"

if act_title == sign_title:
    print("Login is visible")
else: 
    print("Login is not visible")


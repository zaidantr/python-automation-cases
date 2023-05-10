from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

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

login_user = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/h2").is_displayed()
print("'Login to your account' is visible is: ", login_user)

email = "bbutokbuton@gmail.com"
password = "432zenius"

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]").send_keys(email)
driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]").send_keys(password)
driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button").click()

error_msg = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/p")

print("'Your email or password is incorrect!' is visible :", error_msg.is_displayed())
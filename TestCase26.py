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

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

subscribe = driver.find_element(By.XPATH, "//*[@id='footer']/div[1]/div/div/div[2]/div/h2")

print("text SUBSCRIPTION is: ", subscribe.is_displayed())

driver.execute_script("window.scrollTo(0, 0)")

slider = driver.find_element(By.ID, "slider-carousel")

items = slider.find_elements(By.TAG_NAME, "h2")

text_slider = "Full-Fledged practice website for Automation Engineers"

for item in items:
    if item.text == text_slider:
        print("Text is visible")
    else:
        print("Text is not visible")


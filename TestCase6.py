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

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[8]/a").click()

driver.refresh()

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[8]/a").click()

contact = driver.find_element(By.XPATH, "//*[@id='contact-page']/div[2]/div[1]/div/h2")

if contact.is_displayed():
    print("'GET IN TOUCH' is visible")
else: 
    print("'GET IN TOUCH' is not visible")

name = "Butok Buton"
email = "butokbuton@gmail.com"
subject = "Form"
message = "Help Me"

driver.find_element(By.XPATH, "//*[@id='contact-us-form']/div[1]/input").send_keys(name)

driver.find_element(By.XPATH, "//*[@id='contact-us-form']/div[2]/input").send_keys(email)

driver.find_element(By.XPATH, "//*[@id='contact-us-form']/div[3]/input").send_keys(subject)

driver.find_element(By.ID, "message").send_keys(message)

driver.find_element(By.XPATH, "//*[@id='contact-us-form']/div[5]/input").send_keys(r"C:\Users\zaida\Desktop\aaa.jpg")

submit = driver.find_element(By.XPATH, "//*[@id='contact-us-form']/div[6]/input")
driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()

myalert = driver.switch_to.alert
time.sleep(5)
myalert.accept()

success_msg = driver.find_element(By.XPATH, "//*[@id='contact-page']/div[2]/div[1]/div/div[2]")

if success_msg.is_displayed():
    print("'Success! Your details have been submitted successfully.' is visible")
else: 
    print("'Success! Your details have been submitted successfully.' is not visible")

driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[1]/a").click()

act_title = driver.title
homepage_title = "Automation Exercise"

if act_title == homepage_title:
    print("Home Page is visible")
else: 
    print("Home Page is not visible")
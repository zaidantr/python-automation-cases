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

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

subscribe = driver.find_element(By.XPATH, "//*[@id='footer']/div[1]/div/div/div[2]/div/h2")

print("text SUBSCRIPTION is: ", subscribe.is_displayed())

email = "brb@gmail.com"

driver.find_element(By.ID, "susbscribe_email").send_keys(email)

driver.find_element(By.ID, "subscribe").click()

mywait = WebDriverWait(driver,10)

message = mywait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='success-subscribe']/div")))

print("Verify message 'You have been successfully subscribed!:", message.is_displayed())
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

category_section = driver.find_element(By.CLASS_NAME, "left-sidebar")

driver.execute_script("arguments[0].scrollIntoView();", category_section)
if category_section.is_displayed():
    print("Categories are visible on left side bar")
else:
    print("Categories are NOT visible on left side bar")

driver.find_element(By.XPATH, "//*[@id='accordian']/div[1]/div[1]/h4/a/span").click()

time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='Women']/div/ul/li[1]/a").click()

driver.refresh()


driver.find_element(By.XPATH, "//*[@id='accordian']/div[1]/div[1]/h4/a/span").click()

time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='Women']/div/ul/li[1]/a").click()

category_women = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[2]/div/h2")

if category_women.is_displayed():
    print("WOMEN - TOPS PRODUCTS is true")
else:
    print("WOMEN - TOPS PRODUCTS is false")

driver.find_element(By.XPATH, "//*[@id='accordian']/div[2]/div[1]/h4/a/span").click()

time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='Men']/div/ul/li[1]/a").click()

driver.refresh()

category_men = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[2]/div/h2")

if category_men.is_displayed():
    print("User is navigated to that category page is true")
else:
    print("User is navigated to that category page is false")
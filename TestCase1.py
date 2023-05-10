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

new_user = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/h2").is_displayed()
print("'New User Signup!' is visible is: ", new_user)

name = "Butok Buton"
email = "butokbuton@gmail.com"

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[2]").send_keys(name)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]").send_keys(email)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button").click()

enter_account = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div[1]/h2/b").is_displayed()
print("'ENTER ACCOUNT INFORMATION' is visible is: ", enter_account)

gender = "Mr"
password = "432zenius"

radio = driver.find_elements(By.XPATH,"//input[@type='radio']")
# print(len(radio))

for i in radio:
    value = i.get_attribute('value')
    if value == gender:
        i.click()

driver.find_element(By.ID, "password").send_keys(password)

day = "1"
month = "June"
year = "2001"

drp_day = Select(driver.find_element(By.ID, "days"))
drp_day.select_by_value(day)

drp_month = Select(driver.find_element(By.ID, "months"))
drp_month.select_by_visible_text(month)

drp_year = Select(driver.find_element(By.ID, "years"))
drp_year.select_by_visible_text(year)

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print(len(checkboxes))

driver.execute_script("window.scrollBy(0,500)","")

for i in checkboxes:
    i.click()

first_name = "Butok"
last_name = "Buton"
company = "Zenius"
address = "Graha Aktiva Lantai 8"

driver.find_element(By.ID, "first_name").send_keys(first_name)
driver.find_element(By.ID, "last_name").send_keys(last_name)
driver.find_element(By.ID, "company").send_keys(company)
driver.find_element(By.ID, "address1").send_keys(address)
driver.find_element(By.ID, "address2").send_keys(address)

country = "India"

drp_country = Select(driver.find_element(By.ID, "country"))
drp_country.select_by_value(country)

state = "New"
city = "Delhi"
zipcode = "171717"
mobile_number = "08385548484"

driver.find_element(By.ID, "state").send_keys(state)
driver.find_element(By.ID, "city").send_keys(city)
driver.find_element(By.ID, "zipcode").send_keys(zipcode)
driver.find_element(By.ID, "mobile_number").send_keys(mobile_number)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div[1]/form/button").click()

account_created = driver.find_element(By.TAG_NAME, "b").is_displayed()

print("'ACCOUNT CREATED!' is visible is: ", account_created)

driver.refresh()

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a").click()

login_msg = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")

print("Logged in as username is:", login_msg.is_displayed())

driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a").click()

driver.refresh()

account_deleted = driver.find_element(By.TAG_NAME, "b").is_displayed()
print("'ACCOUNT DELETED!' is visible is: ", account_deleted)

driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a").click()
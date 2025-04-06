from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,"fName")
first_name.send_keys("george")
first_name.send_keys(Keys.ENTER)
last_name = driver.find_element(By.NAME,"lName")
last_name.send_keys("paul")
last_name.send_keys(Keys.ENTER)
Email = driver.find_element(By.NAME,"email")
Email.send_keys("Georgepaul@gmail.com")
button = driver.find_element(By.CLASS_NAME, "btn")
button.click()


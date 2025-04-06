from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Deprecated - no longer needed
# chrome_driver_path = "/Users/raam/Development/chromedriver"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
time = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
name = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events = {i: {"time": time[i].text, "name": name[i].text} for i in range(len(time))}

print(events)


# def test_eight_components():
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#     title = driver.title
#     assert title == "Web form"
#     driver.implicitly_wait(0.5)
#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#     text_box.send_keys("Selenium")
#     submit_button.click()
#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

    # Closes Chrome
    # driver.quit()
    # driver.close()


# test_eight_components()

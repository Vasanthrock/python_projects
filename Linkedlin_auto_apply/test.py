# from main import *
# JOIN
# driver.find_element(By.PARTIAL_LINK_TEXT,"Sign in").click()
# RELOAD
# driver.find_element(By.ID,"reload-button")
#
# "https://www.linkedin.com/jobs/search/?currentJobId=4088704442&f_AL=true&f_E=2&f_PP=105214831%2C105556991%2C106888327%2C100100512&f_TPR=r86400&geoId=102713980&keywords=software%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"
#
# # def launch_browser():
# #     driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4088704442&f_AL=true&"
# #            "f_E=2&f_PP=105214831%2C105556991%2C106888327%2C100100512&f_TPR=r86400&geoId=102713980&"
# #            "keywords=software%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
# # launch_browser()
# #
# # try:
# #     joinpage_sign_in = (driver.find_element(By.XPATH, "//*[normalize-space(text())='Sign in']"))
# #     driver.quit()
# #     time.sleep(5)
# #     launch_browser()
# #
# # except NoSuchElementException:
# #    pass
# #
# # try:
# #     e = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/h1')
# #     driver.quit()
# #     time.sleep(5)
# #     launch_browser()
# # #     time.sleep(2)
# # #     joinpage_sign_in = (driver.find_element(By.XPATH, "//*[normalize-space(text())='Sign in']"))
# # #     joinpage_sign_in.click()
# # #
# # except NoSuchElementException:
# #    pass
# # # else:
# # #     time.sleep(5)
# # #     username = driver.find_element(By.ID, "session_key")
# # #     username.send_keys(Email)
# # #     password_field = driver.find_element(By.ID, "session_password")
# # #     password_field.send_keys(password)
# # #     password_field.send_keys(Keys.ENTER)
# # #
# # try:
# #         reload_button=driver.find_element(By.ID,"reload-button")
# #         reload_button.click()
# # except NoSuchElementException:
# #         pass
# # else:
# #     close_button = driver.find_element(By.XPATH,'//*[@id="base-contextual-sign-in-modal"]/div/section/button')
# #     close_button.click()
# #
# #     time.sleep(2)
# #     sign_in_button=driver.find_element(By.LINK_TEXT,"Sign in")
# #     sign_in_button.click()
# #     time.sleep(5)
# #     username= driver.find_element(By.ID,"username")
# #     username.send_keys(Email)
# #     password_field = driver.find_element(By.ID,"password")
# #     password_field.send_keys(password)
# #     password_field.send_keys(Keys.ENTER)
# #
# # try:
# #     close_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/button')
# #     close_button.click()
# # except NoSuchElementException:
# #         pass
# # else:
# #     time.sleep(2)
# #     sign_in_button=driver.find_element(By.LINK_TEXT,"Sign in")
# #     sign_in_button.click()
# #     time.sleep(5)
# #     username= driver.find_element(By.ID,"username")
# #     username.send_keys(Email)
# #     password_field = driver.find_element(By.ID,"password")
# #     password_field.send_keys(password)
# #     password_field.send_keys(Keys.ENTER)
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# # driver.get("https://www.linkedin.com/")
# driver.maximize_window()
#
# sign_in=driver.find_element(By.PARTIAL_LINK_TEXT,"Sign in")
# sign_in.click()
# time.sleep(5)
# username= driver.find_element(By.ID,"username")
# username.send_keys(Email)
# password_field = driver.find_element(By.ID,"password")
# password_field.send_keys(password)
# password_field.send_keys(Keys.ENTER)
#
# time.sleep(2)
# search_icon = driver.find_element(By.XPATH,'//button[@aria-label="Click to start a search"]')
# print(search_icon)
# search_icon.click()
# time.sleep(5)
# search_field = driver.find_element(By.ID,"global-nav-typeahead")
# search_field.send_keys("software developer")
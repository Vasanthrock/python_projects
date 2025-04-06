from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,"cookie")

Money = driver.find_element(By.ID,"money")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]

time_out = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > time_out:

        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_price=[]

        for price in all_prices:
            price_text = price.text
            if price_text != "":
                cost = int(price_text.split("-")[1].strip().replace(",",""))
                item_price.append(cost)

        cookie_upgrade={}
        for i in range(len(item_price)):
            cookie_upgrade[item_price[i]] = items_id[i]

        money_element=driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element=money_element.replace(",","")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost]=id

        highest_price_item = max(affordable_upgrades)
        print(highest_price_item)
        to_purchase_id = affordable_upgrades[highest_price_item]

        driver.find_element(By.ID, to_purchase_id).click()

        time_out = time.time() +5

        if time.time() > five_min:
            cookies_per_second = driver.find_element(By.ID,"cps").text
            print(cookies_per_second)
            break
driver.quit()


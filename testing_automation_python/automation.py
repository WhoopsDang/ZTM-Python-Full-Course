from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


chrome_browser = webdriver.Chrome(options=chrome_options)

chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# This solves the issue with the Popup for those that encounter it:
chrome_browser.implicitly_wait(2)
popup = chrome_browser.find_element(By.ID, "details-button")
popup.click()

proceed = chrome_browser.find_element(By.ID, "proceed-link")

chrome_browser.implicitly_wait(2)
proceed.click()


chrome_browser.implicitly_wait(2)
button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
print(button.get_attribute("innerHTML"))

input_field = chrome_browser.find_element(By.ID, "user-message")
input_field.clear()
input_field.send_keys("I am neat lol")

button.click()

input()

chrome_browser.quit()


# button = chrome_browser.find_element_by_class_name('btn-default')

# button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')

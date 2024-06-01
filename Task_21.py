import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

driver_path = r"D:\Python_HW\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

chrome_options = (Options())
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

#get and display the cookies before login
print("Cookies Before Login:")
cookies_before_login=driver.get_cookies()
for cookie in cookies_before_login:
    print(cookie)

#Login using credentials
username= driver.find_element (By.ID,"user-name")
username.send_keys("standard_user")

passw=driver.find_element(By.ID,"password")
passw.send_keys("secret_sauce")

logins=driver.find_element(By.ID,"login-button")
logins.click()
time.sleep(3)

#Get and display cookies after login
print("\nCookies After Login:")
cookies_after_login=driver.get_cookies()
for cookie in cookies_after_login:
    print(cookie)

#logout
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(3)

#Verifing the cookies after logout
print("\nCookies after logout:")
cookies_after_logout = driver.get_cookies()
for cookie in cookies_after_logout:
    print(cookie)



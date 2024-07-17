
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

def load_page():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

#get and display the cookies before login
def cookies():
    cookies_page=driver.get_cookies()
    for cookie in cookies_page:
        print(cookie)

def login_page():
    #Login using credentials
    username= driver.find_element (By.ID,"user-name")
    username.send_keys("standard_user")
    passw=driver.find_element(By.ID,"password")
    passw.send_keys("secret_sauce")
    logins=driver.find_element(By.ID,"login-button")
    logins.click()
    time.sleep(3)


def logout():
    #logout
    driver.find_element(By.ID,"react-burger-menu-btn").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Logout").click()
    time.sleep(3)

if __name__=="__main__":
    load_page()
    print("Cookies Before Login:")
    cookies()
    login_page()
    print("\nCookies After Login:")
    cookies()
    logout()
    #Verifing the cookies after logout
    print("\nCookies after logout:")
    cookies()







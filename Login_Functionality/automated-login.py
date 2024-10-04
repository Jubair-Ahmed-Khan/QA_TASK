from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

def login():
    url = "https://myalice-automation-test.netlify.app/"
    username = "testuser"
    password = "password"

    driver.get(url)

    username_path = "username"
    username_field = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, username_path))
    )

    password_path = "password"
    password_field = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, password_path))
    )

    login_button_path = "login-btn"
    login_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, login_button_path))
    )

    time.sleep(3)
    username_field.send_keys(username)

    time.sleep(3)
    password_field.send_keys(password)

    time.sleep(5)
    login_button.click()

    time.sleep(8)
    search_path = "manga-search"
    search_box = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, search_path))
    )

    if search_box.is_displayed():
        driver.save_screenshot("login_success.png")
        print("Login successful! Search box found.")


# login
try:
    login()
except Exception as e:
    print("Login failed !!! ", e)
finally:
    driver.quit()


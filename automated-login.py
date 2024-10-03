from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Website URL
url = "https://myalice-automation-test.netlify.app/"

# Login credentials
username = "testuser"
password = "password"

# Webdriver initiate
driver = webdriver.Chrome()

# Visit to the login page
driver.get(url)

try:
    # Find username, password, and login button fields
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-btn"))
    )

    # Enter login credentials with a delay
    time.sleep(3)
    username_field.send_keys(username)

    time.sleep(3)
    password_field.send_keys(password)

    time.sleep(5)
    login_button.click()

    time.sleep(8)
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "manga-search"))
    )

    driver.save_screenshot("login_success.png")

    print("Login successful! Search box found.")

except Exception as e:
    print("Error during login:", e)
    driver.save_screenshot("login_error.png")

finally:
    driver.quit()
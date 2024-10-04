from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

# Function to log in
def login():
    url = "https://myalice-automation-test.netlify.app/"
    username = "testuser"
    password = "password"

    driver.get(url)

    try:
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

    except Exception as e:
        print("Error during login:", e)
        driver.save_screenshot("login_error.png")


# Function to check manga details
def manga_details():
    time.sleep(2)

    span_xpath = '//h3[@id="manga-name"]/following-sibling::p//span[contains(text(), "Details")]'
    span_element = driver.find_element(By.XPATH, span_xpath)
    span_element.click()

    modal_path = '//*[@id="root"]/div/div[3]'
    modal = driver.find_element(By.XPATH, modal_path)

    time.sleep(3)
    if modal.is_displayed():
        driver.save_screenshot("modal.png")
        print("Modal displayed")

        card_title_path = '//*[@id="root"]/div/div[3]/div/h3'
        card_title = driver.find_element(By.XPATH, card_title_path)
        print("Card title = ",card_title.text)

        card_details_path = '//*[@id="root"]/div/div[3]/div/p'
        card_details = driver.find_element(By.XPATH, card_details_path)
        print("Card Details = ", card_details.text)

        time.sleep(3)
        close_button_path = '//*[@id="root"]/div/div[3]/div/button'
        close_button = driver.find_element(By.XPATH, close_button_path)
        close_button.click()

        try:
            modal_path = '//*[@id="root"]/div/div[3]'
            driver.find_element(By.XPATH, modal_path)
        except:
            print("Modal closed")
    else:
        print("Modal not displayed")


# login, display modal with details, and close modal
try:
    login()
    manga_details()
except Exception as e:
    print("Error during showing details:", e)
    driver.save_screenshot("details_error.png")
finally:
    driver.quit()
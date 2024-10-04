from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

# Function to login
def login():

    url = "https://myalice-automation-test.netlify.app/"
    username = "testuser"
    password = "password"

    driver.get(url)

    try:

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-btn"))
        )

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

        if search_box.is_displayed():
            driver.save_screenshot("login_success.png")
            print("Login successful! Search box found.")

    except Exception as e:
        print("Error during login:", e)
        driver.save_screenshot("login_error.png")


# Function to search for manga and verify results
def search_manga(manga_name):

    search_box = driver.find_element(By.ID, 'manga-search')

    if search_box.is_displayed():
        search_box.clear()
        search_box.send_keys(manga_name)

    time.sleep(2)
    search_button = driver.find_element(By.XPATH, '//button[contains(text(),"Search")]')
    search_button.click()

    time.sleep(2)
    manga_cards = driver.find_elements(By.XPATH,
                                       f'//h3[contains(text(),"{manga_name}")]')

    driver.save_screenshot(f"search_result_{manga_name}.png")

    if len(manga_cards) > 0:
        print(f'Search for "{manga_name}" returned {len(manga_cards)} results.')
        for card in manga_cards:
            print(card.text)
    else:
        print(f'No results found for "{manga_name}".')

try:
    login()
    search_manga("Naruto")
    search_manga("One Piece")
    search_manga("Seven Deadly Sins")
    search_manga("No manga found")

except Exception as e:
    print("Error during search:", e)
    driver.save_screenshot("search_error.png")

finally:
    driver.quit()

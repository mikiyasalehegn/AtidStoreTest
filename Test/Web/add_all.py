import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locator.locators import *

ul = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li"
store_page = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[" \
             "1]/div[1]/ul[1]/li[2]/a[1] "


def test_store_link():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://atid.store/")
    driver.maximize_window()

    store_button_locator = driver.find_element(By.XPATH, store_xpath)
    store_button_locator.click()

    actual_store_url = driver.current_url
    assert actual_store_url == "https://atid.store/store/"
    time.sleep(3)

    products = driver.find_elements(By.XPATH, ul)
    amount = len(products)
    assert amount > 1
    time.sleep(1)
    for i, p in enumerate(products):
        locate = f"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[{i + 1}]"
        count = i + 1
        if count <= len(products):
            wait = WebDriverWait(driver, 10)
            pro = wait.until(expected_conditions.presence_of_element_located((By.XPATH, locate)))
            pro.click()
            add_to_cart = driver.find_element(By.XPATH, cart_xpath)
            add_to_cart.click()
            driver.find_element(By.XPATH, store_page).click()
        else:
            break


def test_comment():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://atid.store/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, contact_path).click()
    time.sleep(2)
    driver.find_element(By.XPATH, comment_name).send_keys("mike")
    time.sleep(2)
    driver.find_element(By.XPATH, subject).send_keys("request for help")
    time.sleep(2)
    driver.find_element(By.XPATH, comment_email).send_keys("mikiyasalehegn17@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, comment).send_keys("I need help please")
    time.sleep(2)
    driver.find_element(By.XPATH, send_button).click()
    time.sleep(3)
    thanks = driver.find_element(By.XPATH, thanks_message).text
    assert thanks == "Thanks for contacting us! We will be in touch with you shortly."


# outof_stoke = p.find_element(By.XPATH, "//span[contains(text(),'Out of stock')]")
# if outof_stoke.is_displayed():
#     pass
# else:
#     add_to_cart = driver.find_element(By.XPATH, cart_xpath)
#     add_to_cart.click()
# driver.find_element(By.XPATH, store_page).click()
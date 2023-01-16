import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as e_c, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from Locator.locators import *


@pytest.mark.addtocart
def test_E2E_login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, store_xpath).click()

    actual_store_url = driver.current_url
    assert actual_store_url == "https://atid.store/store/"
    time.sleep(2)
    driver.find_element(By.XPATH, tshirt_xpath).click()

    tishert_name = driver.find_element(By.XPATH, tname_xpath)
    product_name = tishert_name.text
    assert product_name == "ATID Green Tshirt"
    time.sleep(2)
    driver.find_element(By.XPATH, cart_xpath).click()

    price_locator = driver.find_element(By.XPATH, price_xpath)
    actual_text = price_locator.text
    assert actual_text == "190.00 ₪"
    time.sleep(2)
    amount_locator = driver.find_element(By.XPATH, amount_xpath)
    actual_amount = amount_locator.text
    assert actual_amount == "1"
    time.sleep(2)
    driver.find_element(By.XPATH, view_cart_xpath).click()
    time.sleep(2)
    driver.find_element(By.XPATH, checkbutton).click()
    time.sleep(2)
    driver.find_element(By.XPATH, login_xpath).click()
    time.sleep(2)
    driver.find_element(By.XPATH, email_xpath).clear()
    driver.find_element(By.XPATH, email_xpath).send_keys("mikiyasalehegn17@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, passwrd_xpath).clear()
    driver.find_element(By.XPATH, passwrd_xpath).send_keys("1234567")
    time.sleep(2)
    driver.find_element(By.XPATH, logbutton_xpath).click()
    error = driver.find_element(By.XPATH, loginerror).text
    assert error == "Unknown email address. Check again or try your username."


@pytest.mark.addtocart
def test_men_link():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://atid.store/")

    men_link_locator = driver.find_element(By.XPATH, men_xpath)
    men_link_locator.click()

    actual_men_url = driver.current_url
    assert actual_men_url == "https://atid.store/product-category/men/"

    shoe = driver.find_element(By.XPATH, shoe_xpath)
    shoe.click()

    shoe_name = driver.find_element(By.XPATH, sname_xpath)
    product_name = shoe_name.text
    assert product_name == "ATID Blue Shoes"

    add_to_cart = driver.find_element(By.XPATH, cart_xpath)
    add_to_cart.click()

    price_locator = driver.find_element(By.XPATH, price_xpath)
    actual_price = price_locator.text
    assert actual_price == "80.00 ₪"

    amount_locator = driver.find_element(By.XPATH, amount_xpath)
    actual_amount = amount_locator.text
    assert actual_amount == "1"
    time.sleep(2)
    driver.find_element(By.XPATH, view_cart_xpath).click()
    time.sleep(2)
    driver.find_element(By.XPATH, checkbutton).click()
    time.sleep(2)
    name1 = driver.find_element(By.XPATH, fname)
    name1.clear()
    name1.send_keys("Miki")
    name2 = driver.find_element(By.XPATH, lname)
    name2.clear()
    name2.send_keys("Aleh")
    time.sleep(2)
    driver.find_element(By.XPATH, comany).send_keys("Mike")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div["
                                  "1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div["
                                  "1]/div[1]/div[1]/p[4]/span[1]/span[1]/span[1]/span[1]/span[2]").click()

    driver.find_element(By.XPATH, "/html[1]/body[1]/span[2]/span[1]/span[2]/ul[1]/li[109]").click()

    place = driver.find_element(By.XPATH, email)
    place.clear()
    place.send_keys("Gushetsion45")
    time.sleep(2)
    apart = driver.find_element(By.CSS_SELECTOR, home)
    apart.clear()
    apart.send_keys("Haruve")
    posta = driver.find_element(By.XPATH, post)
    posta.clear()
    posta.send_keys("453438")
    time.sleep(2)
    city = driver.find_element(By.XPATH, town)
    city.clear()
    city.send_keys("BeerSheba")

    tel = driver.find_element(By.XPATH, phone)
    tel.clear()
    tel.send_keys("0535024448")
    time.sleep(2)
    emaill = driver.find_element(By.XPATH, email)
    emaill.clear()
    emaill.send_keys("mikeo9@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#place_order").click()
    wait = WebDriverWait(driver, 10)
    wait.until(e_c.visibility_of_element_located((By.XPATH, e_message)))
    err = driver.find_element(By.XPATH, e_message).text
    assert err == "Invalid payment method."



@pytest.mark.addtocart
def test_coupon():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")

    accessories_link_locator = driver.find_element(By.XPATH, access_xpath)
    accessories_link_locator.click()

    bracelet = driver.find_element(By.XPATH, bracelet_xpath)
    bracelet.click()

    add_to_cart = driver.find_element(By.XPATH, cart_xpath)
    add_to_cart.click()

    view_cart = driver.find_element(By.XPATH, view_cart_xpath)
    view_cart.click()
    time.sleep(2)

    coupon_field = driver.find_element(By.XPATH, coupon_xpath)
    coupon_field.send_keys('654651')
    time.sleep(2)

    apply_coupon = driver.find_element(By.XPATH, apply_coupon_xpath)
    apply_coupon.click()
    time.sleep(2)

    error_message = driver.find_element(By.XPATH, error_xpath)
    actual_message = error_message.text
    assert actual_message == 'Coupon "654651" does not exist!'

    time.sleep(2)


def test_rating():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://atid.store/")
    driver.maximize_window()
    store_button_locator = driver.find_element(By.XPATH, store_xpath)
    store_button_locator.click()
    time.sleep(3)

    pros = driver.find_elements(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[4]/ul[1]/li")
    assert len(pros) > 0
    for i, p in enumerate(pros):
        location = f'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/ul[1]/li[{i+1}]/a[1]/span[1]'
        wait = WebDriverWait(driver, 10)
        wait.until(e_c.presence_of_element_located((By.XPATH, f"//li[{i+1}]/div[1]")))
        rate = p.find_element(By.XPATH, f"//li[{i+1}]/div[1]")
        if rate.accessible_name == 'Rated 5.00 out of 5':
            wait.until(e_c.presence_of_element_located((By.XPATH, location)))
            p.find_element(By.XPATH, location).click()
            wait.until(e_c.presence_of_element_located((By.XPATH, cart_xpath)))
            driver.find_element(By.XPATH, cart_xpath).click()
            wait.until(e_c.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/header[1]/div[1]/div["
                                                                  "1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                                                                  "1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")))
            driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                                          "2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
        else:
            pass



def test_star():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://atid.store/")
    driver.maximize_window()
    store_button_locator = driver.find_element(By.XPATH, store_xpath)
    store_button_locator.click()
    time.sleep(3)
    rate = driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[4]/ul[1]/li[1]/div[1]").accessible_name
    assert rate == 'Rated 5.00 out of 5'
    driver.find_element(By.XPATH, "//span[contains(text(),'Boho Bangle Bracelet')]").click()
    time.sleep(3)


def test_store_link():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")

    store_button_locator = driver.find_element(By.XPATH, store_xpath)
    store_button_locator.click()
    driver.execute_script("window.scrollBy(0, 100);")
    driver.find_element(By.XPATH, "//a[contains(text(),'2')]").click()
    wait = WebDriverWait(driver, 10)
    pro = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//body/div[@id='page']/div["
                                                                          "@id='content']/div[1]/div[2]/main[1]/div["
                                                                          "1]/ul[1]/li[1]/div[1]/a[1]/img[1]")))

    pro.click()
    add_to_cart = driver.find_element(By.XPATH, cart_xpath)
    add_to_cart.click()

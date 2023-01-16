import time

from selenium.webdriver.common.by import By
from Base.basepage import BasePage
from Locator.locators import Locators


class AddToCartPage(Locators, BasePage):
    def open(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    def execute_accessories(self):
        self._click(By.XPATH, self.access_xpath)
        self._click(By.XPATH, self.bracelet_xpath)
        assert self.check_product(self.brasname_xpath) == "Buddha Bracelet"
        self._click(By.XPATH, self.cart_xpath)
        self._click(By.XPATH, self.view_cart_xpath)
        self._write(By.XPATH, self.coupon_xpath, '654651')
        self._click(By.XPATH, self.apply_coupon_xpath)
        assert self.message(self.error_xpath) == 'Coupon "654651" does not exist!'

    def execute_store(self):
        self._click(By.XPATH, self.store_xpath)
        self._click(By.XPATH, self.tshirt_xpath)
        assert self.check_product(self.tname_xpath) == "ATID Green Tshirt"
        self._click(By.XPATH, self.cart_xpath)
        self._click(By.XPATH, self.view_cart_xpath)
        self._write(By.XPATH, self.coupon_xpath, 'mg1254')
        self._click(By.XPATH, self.apply_coupon_xpath)
        assert self.message(self.error_xpath) == 'Coupon "mg1254" does not exist!'

    def execute_men(self):
        self._click(By.XPATH, self.men_xpath)
        self._click(By.XPATH, self.shoe_xpath)
        assert self.check_product(self.sname_xpath) == "ATID Blue Shoes"
        self._click(By.XPATH, self.cart_xpath)
        self._click(By.XPATH, self.view_cart_xpath)
        self._write(By.XPATH, self.coupon_xpath, 'sh5478')
        self._click(By.XPATH, self.apply_coupon_xpath)
        assert self.message(self.error_xpath) == 'Coupon "sh5478" does not exist!'

    def execute_women(self):
        self._click(By.XPATH, self.women_xpath)
        self._click(By.XPATH, self.bag_xpath)
        assert self.check_product(self.bname_xpath) == "Black Over-the-shoulder Handbag"
        self._click(By.XPATH, self.cart_xpath)
        self._click(By.XPATH, self.view_cart_xpath)
        self._write(By.XPATH, self.coupon_xpath, 'sh5478')
        self._click(By.XPATH, self.apply_coupon_xpath)
        assert self.message(self.error_xpath) == 'Coupon "sh5478" does not exist!'

    def execute_comment(self):
        self._click(By.XPATH, self.contact_path)
        self._write(By.XPATH, self.comment_name, 'Mike')
        self._write(By.XPATH, self.subject, "request for help")
        self._write(By.XPATH, self.comment_email, "mikiyasalehegn17@gmail.com")
        self._write(By.XPATH, self.comment, "I need help please")
        self._click(By.XPATH, self.send_button)
        assert self.message(self.thanks_message) == "Thanks for contacting us! We will be in touch with you shortly."

    def execute_e2e_login(self):
        self._click(By.XPATH, self.women_xpath)
        self._click(By.XPATH, self.bag_xpath)
        assert self.check_product(self.bname_xpath) == "Black Over-the-shoulder Handbag"
        self._click(By.XPATH, self.cart_xpath)
        self._click(By.XPATH, self.view_cart_xpath)
        self._click(By.XPATH, self.checkbutton)
        self._click(By.XPATH, self.login_xpath)
        self._write(By.XPATH, self.email_xpath, "mikiyasalehegn17@gmail.com")
        self._write(By.XPATH, self.passwrd_xpath, "1234567")
        self._click(By.XPATH, self.logbutton_xpath)
        assert self.message(self.loginerror) == "Unknown email address. Check again or try your username."

    def execute_e2e_register(self):
        self._click(By.XPATH, self.men_xpath)
        self._click(By.XPATH, self.shoe_xpath)
        assert self.check_product(self.sname_xpath) == "ATID Blue Shoes"
        self._click(By.XPATH, self.cart_xpath)
        assert self.check_product(self.price_xpath) == "80.00 ₪"
        self._click(By.XPATH, self.view_cart_xpath)
        self._click(By.XPATH, self.checkbutton)
        self._write(By.XPATH, self.fname, "Miki")
        self._write(By.XPATH, self.fname, "Aleh")
        self._write(By.XPATH, self.fname, "Mike")
        self._click(By.XPATH, self.country)
        self._click(By.XPATH, self.israel)
        self._write(By.XPATH, self.fname, "Gushetsion45")
        self._write(By.XPATH, self.fname, "Haruve")
        self._write(By.XPATH, self.fname, "453438")
        self._write(By.XPATH, self.fname, "BeerSheba")
        self._write(By.XPATH, self.fname, "0535024448")
        self._write(By.XPATH, self.fname, "mikeo9@gmail.com")
        self._click(By.XPATH, self.place_order_button)
        assert self.message(self.e_message) == "Invalid payment method."

    def execute_add_all(self):
        self._click(By.XPATH, self.access_xpath)
        products = self._driver.find_elements(By.XPATH, self.ul)
        for i, p in enumerate(products):
            locate = f"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[{i + 1}]"
            count = i + 1
            if count <= len(products):
                self._click(By.XPATH, locate)
                self._click(By.XPATH, self.cart_xpath)
                self._click(By.XPATH, self.access_xpath)
            else:
                break

    def execute_5star(self):
        self._click(By.XPATH, self.store_page)
        time.sleep(3)
        pros = self._driver.find_elements(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[4]/ul[1]/li")
        time.sleep(3)
        for i in range(len(pros)):
            location = f'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/ul[1]/li[{i+1}]/a[1]/span[1]'
            rating = self._find(By.XPATH, f"//li[{i+1}]/div[1]").accessible_name
            if rating == 'Rated 4.67 out of 5':
                self._click(By.XPATH, location)
                time.sleep(3)
                self._click(By.XPATH, self.cart_xpath)
                self._click(By.XPATH, self.store_page)
                time.sleep(3)
            else:
                pass

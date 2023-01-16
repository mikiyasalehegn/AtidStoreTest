from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def _find(self, by, locate) -> WebElement:
        return self._driver.find_element(by, locate)

    def _write(self, by, locate, content):
        self._driver.find_element(by, locate).send_keys(content)

    def _click(self, by, locate):
        self._wait_until_element_is_visible(locate)
        self._find(by, locate).click()

    def _wait_until_element_is_visible(self, locate, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(e_c.visibility_of_element_located((By.XPATH, locate)))

    def message(self, error):
        self._wait_until_element_is_visible(error)
        return self._find(By.XPATH, error).text

    def check_product(self, errpath):
        self._wait_until_element_is_visible(errpath)
        return self._find(By.XPATH, errpath).text

    def is_displayed(self, by, locate):
        try:
            return self._find(by, locate).is_displayed()
        except NoSuchElementException:
            return False

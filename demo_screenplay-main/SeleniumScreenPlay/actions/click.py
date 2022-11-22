from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Click:
    def Click(self, driver: webdriver, locator, button):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, locator))).send_keys(text)
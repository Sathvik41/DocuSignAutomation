from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class Login_Page():
    def __init__(self, driver):
        self.driver = driver

        self.user_name = "input[data-qa='username']"
        self.submit_userName = "button[data-qa='submit-username']"
        self.password = "input[data-qa='password']"
        self.submit_password = "button[data-qa='submit-password']"
        self.home_page_title = "header-home-desktop"

    def login_page(self, userName, password):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.user_name))).send_keys(userName)
        # driver = self.driver
        # user1 = Login_Page(driver)
        # user1.set_textField(self, "input[data-qa='username']", "Testing")

        self.driver.find_element(By.CSS_SELECTOR, self.submit_userName).click()
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.password))).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.submit_password).click()
        time.sleep(5)

    # def set_textField(self.id, inputValue):
    #     WebDriverWait(self.driver, 60).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, self.id))).send_keys(inputValue)


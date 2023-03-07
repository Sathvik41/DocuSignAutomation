from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
import time


class Add_Signature():
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.signature_field = "button[data-qa='Signature']"
        self.select_approver2 = "button[data-qa='recipient-2']"
        self.send_button = "button[data-qa='footer-send-button']"
        self.home_page = "button[data-qa='header-HOME-tab-button']"
        self.recipient_selector = "button[data-qa='recipient-selector']"
        self.success_message = "//div[@data-qa='ds-toast-content-text']"
        self.formatting_button = "(//button[@class='css-v243cw'])[2]"
        self.dimension_scale = "//input[@data-qa='data-dimension-scale']"
        self.banner_no_thanks_button = "button[data-qa='banner-button-secondary']"

    def add_signature(self):
        source = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.signature_field)))
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_by_offset(400, 130).pause(2).move_by_offset(-10, -10).release().perform()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.recipient_selector).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_approver2))).click()
        source = self.driver.find_element(By.CSS_SELECTOR, self.signature_field)
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_by_offset(650, 130).pause(2).move_by_offset(-10, -10).release().perform()
        time.sleep(2)
        self.driver.save_screenshot('./screenshots/Add_SignatureTags.png')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.send_button))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.banner_no_thanks_button))).click()
        # Step - TST2-3
        success_msg = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((
            By.XPATH, self.success_message))).text

        # assert success_msg == constants.success_message
        self.driver.save_screenshot('./screenshots/Send_Envelope.png')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.home_page))).click()

    def change_signature_tag_size(self):
        source = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.signature_field)))
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_by_offset(400, 270).pause(2).move_by_offset(-10, -10).release().perform()
        time.sleep(2)
        self.driver.save_screenshot('./screenshots/SignatureTag_size_before_changes.png')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.formatting_button))).click()
        dimension_scale = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.dimension_scale)))
        dimension_scale.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
        dimension_scale.send_keys("200")
        self.driver.find_element(By.CSS_SELECTOR, self.recipient_selector).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_approver2))).click()
        source = self.driver.find_element(By.CSS_SELECTOR, self.signature_field)
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_by_offset(650, 270).pause(2).move_by_offset(-10, -10).release().perform()
        time.sleep(2)
        dimension_scale = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.dimension_scale)))
        dimension_scale.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
        dimension_scale.send_keys("200")
        time.sleep(2)
        self.driver.save_screenshot('./screenshots/SignatureTag_size_after_changes.png')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.send_button))).click()
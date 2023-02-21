from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
from utilities.generateutils import generate_string
import logging as logger
import time


class Audit_Logs():
    def __init__(self, driver):
        self.driver = driver

        # Locators:
        self.settings_tab = "//button[@data-qa='header-RADMIN-tab-button']"
        self.audit_log = "//button[@data-qa='nav_link_authenticated.audit-log']"
        self.filter_button = "//button[@data-qa='filter_control_filter_btn']"
        self.audit_log_event_date = "select[data-qa='audit-logs-event-date']"
        self.apply_button = "button[data-qa='filter_apply_btn']"
        self.logs_row = "//tr[@data-qa='row_0']"
        self.users_tab = "//button[@data-qa='nav_link_authenticated.users']"
        self.edit_user = "//div[contains (text(), 'Docusign Approver1')]"
        self.postal_code = "//input[@data-qa='edit_user_postal_code_txb']"
        self.save_button = "//button[@data-qa='ds_ackbar_save_btn']"
        self.accept_cookies_user = "//button[@class='optanon-allow-all accept-cookies-button']"
        self.company_field = "(//input[@class='css-1h48rq'])[3]"
        self.new_value_cell = "//td[@data-qa='New Value_cell']"

    def verify_auditLogs(self):
        settingsTab = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, self.settings_tab)))
        time.sleep(5)
        settingsTab.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.users_tab))).click()
        time.sleep(5)
        parent_window = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in main_window:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.accept_cookies_user))).click()
        self.driver.switch_to.window(parent_window)
        random_info = generate_string()
        logger.info(random_info)
        company_name_field = random_info['company_name']
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.edit_user))).click()
        companyField = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.company_field)))
        companyField.clear()
        companyField.send_keys(company_name_field)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.save_button))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.audit_log))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.filter_button))).click()
        dropDown = self.driver.find_element(By.CSS_SELECTOR, self.audit_log_event_date)
        selectValue = Select(dropDown)
        selectValue.select_by_visible_text(constants.customFilter)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.apply_button))).click()
        self.driver.save_screenshot("./screenshots/Audit_Logs.png")
        time.sleep(5)
        audit_logs_new_value = self.driver.find_element(By.XPATH, self.new_value_cell).text
        print(audit_logs_new_value)
        assert company_name_field == audit_logs_new_value
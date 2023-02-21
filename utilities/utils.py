import csv
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from testData import constants as constants
import logging as logger
import random
import string
import pandas as pd
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


class Util_Test():
    def __init__(self, driver):
        self.driver = driver

        # Locators:
        self.profile_button = "//button[@data-qa='header-profile-menu-button']"
        self.logoff_button = "button[data-qa='header-logoff-button']"
        self.settings_tab = "//button[@data-qa='header-RADMIN-tab-button']"
        self.regional_settings_field = "//button[@data-qa='nav_link_authenticated.regional-settings']"
        self.regional_settings = "//button[@data-qa='regional-settings']"
        self.allow_user_set_time_zone_format = \
            "//button[@data-qa='regional_settings_allow_user_to_set_time_zone_format_cb']"
        self.dat_time_format_dropdown = "//select[@data-qa='date-time-format-dropdown']"

    def read_data_from_csv(self, filename):
        date_time_columns = pd.read_csv(filename, usecols=[
            'Sent On (Date)', 'Sent On (Time)', 'Last Activity (Date)', 'Last Activity (Time)', 'Completed On (Date)',
            'Completed On (Time)'])
        print(date_time_columns)
        assert "Sent On (Date)" in date_time_columns
        assert "Sent On (Time)" in date_time_columns
        assert "Last Activity (Date)" in date_time_columns
        assert "Last Activity (Time)" in date_time_columns
        assert "Completed On (Date)" in date_time_columns
        assert "Completed On (Time)" in date_time_columns
        self.driver.save_screenshot('./screenshots/Envelope_csv_report.png')

    def logout(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((
            By.XPATH, self.profile_button))).click()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, self.logoff_button))).click()

    def scroll_page(self):
        self.driver.find_element('css selector', "button[data-qa='tutorial-got-it']").click()
        time.sleep(5)
        self.driver.execute.script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    def switch_to_window(self):
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
                yield
        self.driver.switch_to.window(parentWindow)

    def timeZone_dateFormat(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.settings_tab))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.regional_settings_field))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.allow_user_set_time_zone_format))).click()

    def my_preferences(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.my_preferences))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.regional_settings))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.date_time_format))).Editable




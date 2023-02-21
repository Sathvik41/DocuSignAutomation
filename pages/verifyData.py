from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
import time


class Envelope_History():
    def __init__(self, driver):
        self.driver = driver

        # Locators:
        self.manage_tab = "//button[@data-qa='header-MANAGE-tab-button']"
        self.sent_box = "button[data-qa='manage-sidebar-labels-sent-label']"
        self.select_envelope_docx = "//div[contains(text(), " + constants.envelope_file_docx + ")]"
        self.open_document = "//a[@data-qa='page-thumbnail']"
        self.more_document = "button[data-qa='document-more']"
        self.envelope_action_history = "button[data-qa='envelope-action-history']"
        self.history_activity_row = "tr[data-qa='history-activity-row']"
        self.user_name_text = "(//td[contains(text(), 'Docusign Sender')])[1]"
        self.signature_id = "//td[contains(text(), '54cfffe6-35eb-4dd9-81e8-35ab08e0e62e')]"
        self.adopted_signature_id = "//td[contains(text(), '723bde61-2321-43f8-af2a-4d5a04843d65')]"
        self.close_button = "//button[@data-qa='history-modal-close']"
        self.reports_tab = "//button[@data-qa='header-REPORTS-tab-button']"
        self.envelope_button = "//button[@data-qa='Envelope']"
        self.view_button = "(//a[@data-qa='report-action'])[1]"
        self.report_range_menu = "button[data-qa='report-range-menu']"
        self.date_range_any = "button[data-qa='date_range_any']"
        self.date_range_custom = "button[data-qa='date_range_custom']"
        self.date_range_from_button = "button[data-qa='date-range-from-button']"
        self.day_picker = "(//div[@aria-selected='true'])[1]"
        self.present_day_checkbox = "//label[@data-qa='present-day-checkbox-label']"
        self.run_report = "button[data-qa='run-report']"
        self.report_result = "(//tr[@data-qa='report-result-row'])[1]"
        self.report_download = "//button[@data-qa='report-download-icon']"
        self.user_label = "//span[contains(text(), 'User')]"
        self.profile_icon = "//span[@data-qa='header-profile-menu-button-avatar']"
        self.my_preferences = "//button[@data-qa='header-choice-PREFERENCES-button']"
        self.regional_settings = "//button[@data-qa='regional-settings']"
        self.date_time_format = "//select[@data-qa='date-time-format-dropdown']"
        self.home_tab = "//span[@data-qa='header-HOME-tab-button-text']"
        self.action_required = "//button[@data-qa='action-required-count']"
        self.settings_tab = "//a[@data-qa='header-RADMIN-tab-button-text']"
        self.users_option = "//button[@data-qa='nav_link_authenticated.users']"
        self.add_user = "//button[@data-qa='users_add_user_btn']"
        self.user_email_text_box = "//input[@data-qa='add-user-email-textbox']"
        self.add_user_next_btn1 = "//button[@data-qa='add_user_step1_next_btn']"
        self.full_name_text_box = "//input[@class='css-1h48rq']"
        self.add_user_next_btn2 = "//button[@data-qa='add_user_step2_next_btn']"
        self.access_code_text_box = "//input[@class='css-1h48rq']"
        self.permission_profile_dropdown = "//select[@data-qa='add_user_ps_selector']"
        self.add_user_next_btn3 = "//button[@data-qa='add_user_step3_next_btn']"
        self.add_user_next_btn4 = "//button[@data-qa='add_user_step4_next_btn']"
        self.email_preferences = "//button[@data-qa='nav_link_authenticated.email-preferences']"
        self.users_list_page = "//h1[@data-qa='accountUserList_page_title']"
        self.email_preferences_checkbox1 = "(//label[@class='css-1n0yh7u'])[2]"
        self.email_preferences_checkbox2 = "(//label[@class='css-1n0yh7u'])[3]"
        self.save_button = "//[@data-qa='ds_ackbar_save_btn']"
        self.email_preferences_title = "//[@data-qa='email-preferences_page_title']"

    # Verify date format on Envelop
    def verify_dateFormat(self):
        manageTab = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.XPATH, self.manage_tab)))
        manageTab.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sent_box))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.open_document))).click()
        time.sleep(10)
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                childWindow = handle
                self.driver.switch_to.window(childWindow)
        self.driver.save_screenshot("./screenshots/date_format.png")
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(parentWindow)

    # Verify Envelope history
    def verify_envelope_history(self):
        manageTab = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, self.manage_tab)))
        manageTab.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sent_box))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.more_document))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.envelope_action_history))).click()
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        label1 = self.driver.find_element(By.XPATH, self.user_label)
        time.sleep(2)
        self.driver.save_screenshot("./screenshots/UserName_UserAPI.png")
        scroll_origin = ScrollOrigin.from_element(label1)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 500).perform()
        time.sleep(5)
        self.driver.save_screenshot("./screenshots/Signature_AdoptedSignature_IDs.png")
        userLabel = self.driver.find_element(By.XPATH, self.user_label).text
        print(userLabel)
        text_userName = self.driver.find_element(By.XPATH, self.user_name_text).text
        print(text_userName)
        assert constants.senderName in text_userName
        # assert constants.userAPI in text_userName
        text_signatureID = self.driver.find_element(By.XPATH, self.signature_id).text
        print(text_signatureID)
        assert constants.signatureID in text_signatureID
        assert constants.adoptedSignatureID in text_signatureID
        self.driver.find_element(By.XPATH, self.close_button).click()
        self.driver.switch_to.window(parentWindow)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.reports_tab))).click()
        # Step 5-Test case2-4
        reports_page = self.driver.current_url
        print(reports_page)
        assert reports_page == constants.reports
        self.driver.save_screenshot("./screenshots/Reports_page.png")
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, self.envelope_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.view_button))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.report_range_menu))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.date_range_custom))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.present_day_checkbox))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.run_report))).click()
        report_result = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.report_result))).text
        print(report_result)
        download = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.report_download)))
        self.driver.execute_script("arguments[0].click();", download)

    def test_case2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.my_preferences))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.regional_settings))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.date_time_format)))
        # TST-3
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.settings_tab))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.users_option))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, self.user_email_text_box))).send_keys("testemail1@pharmateksol.com")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn1))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, self.full_name_text_box))).send_keys("Test User1")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn2))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.access_code_text_box))).send_keys("12345")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn3))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn4))).click()
        users_list = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn4))).text
        assert users_list == "Users"
        user_name = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/td[contains(.,'Test User1')]")))
        print(user_name)
        self.driver.save_screenshot("./screenshots/UsersList_page.png")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.email_preferences))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.email_preferences_checkbox1))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.email_preferences_checkbox2))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.save_button))).click()
        email_pre = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.email_preferences_title))).text
        print(email_pre)
        self.driver.save_screenshot("./screenshots/email_preferences_page.png")


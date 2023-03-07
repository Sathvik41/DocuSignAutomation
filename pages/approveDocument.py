from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.loginPage import Login_Page
from testData import constants as constants
from utilities.utils import Util_Test
import time


class Approve_Envelope():
    def __init__(self, driver):
        self.driver = driver

        # Elements:
        self.manage_tab = "//button[@data-qa='header-MANAGE-tab-button']"
        self.action_required = "button[data-qa='action-required-count']"
        self.select_envelope_docx = "//div[contains(text(), " + constants.envelope_file_docx + ")]"
        self.select_envelope_pdf = "//div[contains(text(), " + constants.envelope_file_pdf + ")]"
        self.sign_button = "button[data-qa='status-action-button-sign']"
        self.continue_button = "action-bar-btn-continue"
        self.navigate_option = "navigate-btn"
        self.sign_option = "//*[contains(@class, 'signature-tab-content')]"
        self.signing_reason = "signingReason"
        self.select_signing_reason = "//*[contains(text(),'I approve')]"
        self.dialog_submit = "button[data-qa='dialog-submit']"
        self.cfr_continue_button = "button[data-qa='cfr-continue']"
        self.finish_button = "//button[@data-qa='slide-up-bar-finish-button']"
        self.no_thanks_text = "//span[@data-qa='sign-next-no-thanks-text']"
        self.no_thanks_button = "//button[@data-qa='sign-next-no-thanks']"
        self.docusign_header = "//a[@data-qa='header-docusign-home-link']"
        self.home_tab = "//button[@data-qa='header-HOME-tab-button']"
        self.other_actions = "//button[@data-qa='toggle-other-actions']"
        self.decline_to_sign = "(//button[@data-qa='show-decline-warning'])[2]"
        self.decline_continue_button = "//button[@data-qa='show-decline-to-sign']"
        self.decline_reason_text_box = "//textarea[@data-qa='decline-dialog-reason-text']"
        self.decline_to_sign_button = "//button[@data-qa='decline-dialog-decline-to-sign']"
        self.document_status = "//span[@data-qa='detail-status-title']"
        self.more_dropDown = "//button[@data-qa='document-more']"
        self.void_option = "//button[@data-qa='envelope-action-void']"
        self.void_reason_box = "//*[@data-qa='input-reason-for-voiding']"
        self.void_button = "//button[@data-qa='modal-confirm-btn']"

    def approve_document(self, docx=False):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.action_required))).click()
        if docx:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        else:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.select_envelope_pdf))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sign_button))).click()

    def esign_approver1(self, noThanksButton=False):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, self.continue_button))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.navigate_option))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_option))).click()
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        drop_down = self.driver.find_element(By.ID, self.signing_reason).is_clickable()
        select_method = Select(drop_down)
        select_method.select_by_visible_text(constants.signingReason)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dialog_submit))).click()
        self.driver.save_screenshot('./screenshots/Click_Sign_Approver1.png')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.cfr_continue_button))).click()
        all_windows = self.driver.window_handles
        current_window = all_windows[0]
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)
        login = Login_Page(self.driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        self.driver.switch_to.window(current_window)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.finish_button))).click()
        if noThanksButton:
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, self.no_thanks_button))).click()
        else:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, self.manage_tab)))
        # WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.home_tab))).click()
        # import pdb
        # pdb.set_trace()

    def esign_approver2(self, noThanksButton=False):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.continue_button))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.navigate_option))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_option))).click()
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        drop_down = self.driver.find_element(By.ID, self.signing_reason)
        select_method = Select(drop_down)
        select_method.select_by_visible_text(constants.signingReason)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dialog_submit))).click()
        self.driver.save_screenshot('./screenshots/Click_Sign_Approver2.png')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.cfr_continue_button))).click()
        all_windows = self.driver.window_handles
        current_window = all_windows[0]
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)
        login = Login_Page(self.driver)
        login.login_page(constants.approver2Email, constants.approver2Password)
        self.driver.switch_to.window(current_window)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.finish_button))).click()
        time.sleep(40)
        if noThanksButton:
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, self.no_thanks_button))).click()
        else:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, self.manage_tab)))

    def complete_esign_approver(self):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, self.finish_button))).click()
        time.sleep(5)
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        try:
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.no_thanks_button))).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def decline_envelope(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.other_actions))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.decline_to_sign))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.decline_continue_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.decline_reason_text_box))).send_keys(constants.decline_reason)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.decline_to_sign_button))).click()
        doc_status = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((
            By.XPATH, self.document_status))).text
        self.driver.save_screenshot('./screenshots/Decline_Envelope.png')
        print(doc_status)
        assert doc_status == constants.decline_status

    def void_envelope(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.manage_tab))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.more_dropDown))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.void_option))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.void_reason_box))).send_keys('Testing')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.void_button))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        document_status = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.document_status))).text
        print(document_status)
        self.driver.save_screenshot('./screenshots/Voided_Envelope.png')
        assert document_status == 'Voided'










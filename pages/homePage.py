from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
import time
import os


class Home_Page():
    def __init__(self, driver):
        self.driver = driver

        self.send_documents_for_signature = "/div[@class='css-vrm39m']"
        self.start_button = "button[data-qa='manage-sidebar-actions-ndse-trigger']"
        self.send_envelope = "button[data-qa='manage-sidebar-actions-ndse-send_envelope']"
        self.upload_file_button = "button[data-qa='upload-file-button']"
        self.browse_button = "label[class='css-rpxvy8']"
        self.add_recipients = "button[data-qa='recipients-add']"
        self.set_signing_order = "focusStyles"
        self.recipient_routing_order1 = "(//input[@data-qa='recipient-routing-order'])[1]"
        self.recipient_routing_order2 = "(//input[@data-qa='recipient-routing-order'])[2]"
        self.recipient_name1 = "(//input[@data-qa='recipient-name'])[1]"
        self.recipient_name2 = "(//input[@data-qa='recipient-name'])[2]"
        self.recipient_email1 = "(//input[@data-qa='recipient-email'])[1]"
        self.recipient_email2 = "(//input[@data-qa='recipient-email'])[2]"
        self.next_button = "button[data-callout='footer-prepare-next-action']"
        self.upload_file_input = "input[data-qa='upload-file-input']"
        self.wootric_close_button = "wootric-close"
        self.add_recipients_content = "button[aria-controls='add-recipients-content']"
        self.select_envelope_docx = "//div[contains(text(), " + constants.envelope_file_docx + ")]"
        self.select_envelope_pdf = "//div[contains(text(), " + constants.envelope_file_pdf + ")]"
        self.correct_button = "button[data-qa='status-action-button-correct']"
        self.correct_resend_button = "button[data-qa='footer-simple-correct-resend-link']"
        self.manage_tab = "button[data-qa='header-MANAGE-tab-button']"
        self.approver_name1 = "(//span[@data-qa='recipient-name'])[2]"
        self.approver_name2 = "(//span[@data-qa='recipient-name'])[1]"

    def upload_envelope_documents(self, name_appr1, email_appr1, name_appr2, email_appr2, docFile=False,
                                  wootricPopup=False):
        # T2-TST 1 - step1:42-44
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.start_button)))
        homePage = self.driver.current_url
        assert homePage == constants.homePage
        print(homePage)
        self.driver.save_screenshot("./screenshots/home_page.png")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.start_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.send_envelope))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.upload_file_button))).click()
        browse_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.upload_file_input)))
        if docFile:
            absolute_file_path_docx = os.path.abspath(constants.upload_envelope_docx)
            browse_button.send_keys(absolute_file_path_docx)
        else:
            absolute_file_path_pdf = os.path.abspath(constants.upload_envelope_pdf)
            browse_button.send_keys(absolute_file_path_pdf)
        time.sleep(10)
        if wootricPopup:
            self.driver.find_element(By.ID, self.wootric_close_button).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.add_recipients_content)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.set_signing_order))).click()
        self.driver.save_screenshot('./screenshots/Add_Envelope.png')
        self.driver.find_element(By.CSS_SELECTOR, self.add_recipients).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_name1))).send_keys(name_appr1)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_email1))).send_keys(email_appr1)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_name2))).send_keys(name_appr2)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_email2))).send_keys(email_appr2)
        time.sleep(2)
        self.driver.save_screenshot('./screenshots/Set_Signing_Order.png')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.next_button))).click()

    def upload_document2(self, name_app1, email_app1, name_app2, email_app2, docfile=False):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.start_button))).click()
        self.driver.find_element(By.CSS_SELECTOR, self.send_envelope).click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, self.upload_file_button).click()
        time.sleep(5)
        browse_button = self.driver.find_element(By.CSS_SELECTOR, self.upload_file_input)
        time.sleep(5)
        if docfile:
            browse_button.send_keys(constants.upload_envelope_docx)
        else:
            browse_button.send_keys(constants.upload_envelope_pdf)
        time.sleep(2)
        self.driver.find_element(By.ID, self.wootric_close_button)
        self.driver.find_element(By.CLASS_NAME, self.set_signing_order).click()
        self.driver.find_element(By.CSS_SELECTOR, self.add_recipients).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.recipient_name1).send_keys(name_app1)
        self.driver.find_element(By.XPATH, self.recipient_email1).send_keys(email_app1)
        self.driver.find_element(By.XPATH, self.recipient_name2).send_keys(name_app2)
        self.driver.find_element(By.XPATH, self.recipient_email2).send_keys(email_app2)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.next_button).click()
        time.sleep(2)

    def change_routing_order(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.manage_tab))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.correct_button))).click()
        routing_order1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_routing_order1)))
        routing_order1.send_keys(Keys.BACKSPACE)
        routing_order1.send_keys("2")
        time.sleep(2)
        routing_order2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_routing_order2)))
        routing_order2.send_keys(Keys.BACKSPACE)
        routing_order2.send_keys("1")
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.next_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.correct_resend_button))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        approver2 = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.approver_name2))).text
        print(approver2)
        assert approver2 == "Docusign Approver2"
        approver1 = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.approver_name1))).text
        print(approver1)
        assert approver1 == "Docusign Approver1"
        self.driver.save_screenshot('./screenshots/Change_Signing_Order.png')

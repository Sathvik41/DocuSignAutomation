import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait

from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.addSign import Add_Signature
from pages.approveDocument import Approve_Envelope
from pages.auditLogs import Audit_Logs
from pages.verifyData import Envelope_History
from ecdsa import SigningKey
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
from selenium.webdriver.common.by import By
import time
import aspose.words as aw
from api_example_base import ApiExampleBase, MY_DIR


@pytest.mark.usefixtures("test_setup")
class Test_DocuSign():
    def test_docuSign(self):
        driver = self.driver
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.senderEmail, constants.senderPassword)

    def test_pdf(self):

        manageTab = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((
            By.XPATH, "//button[@data-qa='header-MANAGE-tab-button']")))
        manageTab.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[data-qa='manage-sidebar-labels-sent-label']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, "//div[contains(text(), " + constants.envelope_file_docx + ")]"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, "//a[@data-qa='page-thumbnail']"))).click()
        time.sleep(10)
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                childWindow = handle
                self.driver.switch_to.window(childWindow)

        get_current_url = self.driver.current_url
        resp = requests.get(get_current_url)
        print('current url:', get_current_url)
        doc = aw.Document(docs_base.my_dir + get_current_url)
        if resp.status_code == 200:
            print("Page opened successfully")
        else:
            print("Page not opened")
        private_key = SigningKey.generate()  # uses NIST192p
        signature = private_key.sign(b"Educative authorizes this shot")
        print('sign:', signature)
        public_key = private_key.verifying_key
        print("Verified:", public_key.verify(signature, b"Educative authorizes this shot"))

        # doc = PDFDoc(in_docpath)
        # opts = VerificationOptions(VerificationOptions.e_compatibility_and_archiving)
        # opts.AddTrustedCertificate(in_public_key_file_path)
        # result = doc.VerifySignedDigitalSignatures(opts)

        '''soup = BeautifulSoup(resp.text, 'html.parser')
        a=soup.find('ul',{"class":"endOfContent active"})
        for i in a.find_all('div'):
            print(i.text)
        else:
            print('Error')'''
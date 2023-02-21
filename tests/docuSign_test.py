from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.addSign import Add_Signature
from pages.approveDocument import Approve_Envelope
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_DocuSign():
    def test_docuSign(self):
        driver = self.driver
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.senderEmail, constants.senderPassword)

        # Upload docx envelope file
        home = Home_Page(driver)
        home.upload_envelope_documents(
            constants.approver1Name, constants.approver1Email, constants.approver2Name, constants.approver2Email,
            True, False)
        sign = Add_Signature(driver)
        sign.add_signature()
        # user = Util_Test(driver)
        # user.logout()

        # Upload pdf envelope file
        home = Home_Page(driver)
        home.upload_envelope_documents(
            constants.approver1Name, constants.approver1Email, constants.approver2Name, constants.approver2Email, False,
            False)
        sign = Add_Signature(driver)
        sign.add_signature()
        home.change_routing_order()
        user = Util_Test(driver)
        user.logout()

        # Login as approver2 and complete e-sign
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.approver2Email, constants.approver2Password)
        approve = Approve_Envelope(driver)
        approve.approve_document(True)
        login = Login_Page(driver)
        login.login_page(constants.approver2Email, constants.approver2Password)
        sign = Approve_Envelope(driver)
        sign.esign_approver2(False)
        # complete = Approve_Envelope(driver)
        # complete.complete_esign_approver(True)
        user = Util_Test(driver)
        user.logout()

        # Login as approver1 and complete e-sign
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        approve = Approve_Envelope(driver)
        approve.approve_document(True)
        self.driver.save_screenshot('./screenshots/Review_Doc_Approver2.png')
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        sign = Approve_Envelope(driver)
        sign.esign_approver1(True)
        # complete = Approve_Envelope(driver)
        # complete.complete_esign_approver(False)
        # user = Util_Test(driver)
        # user.logout()

        # Verify data:
        '''self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.senderEmail, constants.senderPassword)
        data = Envelope_History(driver)
        data.verify_dateFormat()

        # Verify Envelope history
        data = Envelope_History(driver)
        data.verify_envelope_history()

        # Verify Audit logs
        logs = Audit_Logs(driver)
        logs.verify_auditLogs()
        csv = Util_Test(driver)
        csv.read_data_from_csv(constants.csv_envelope_report)'''

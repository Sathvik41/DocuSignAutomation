from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.addSign import Add_Signature
from pages.approveDocument import Approve_Envelope
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_DeclineEnvelope():
    def test_declineEnvelope(self):

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
        user = Util_Test(driver)
        user.logout()

        # Login as approver1 and decline e-sign
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        decline = Approve_Envelope(driver)
        decline.approve_document(True)
        login.login_page(constants.approver1Email, constants.approver1Password)
        decline.decline_envelope()

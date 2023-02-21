import pytest
from pages.loginPage import Login_Page
from testData import constants as constants
from pages.auditLogs import Audit_Logs
from pages.verifyData import Envelope_History
from utilities.utils import Util_Test


@pytest.mark.usefixtures("test_setup")
class Test_EnvelopeHistory():
    def test_verify_envelopeHistory_auditLogs(self):

        # Verify data:
        driver = self.driver
        self.driver.get(constants.baseUrl)
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
        csv.read_data_from_csv(constants.csv_envelope_report)

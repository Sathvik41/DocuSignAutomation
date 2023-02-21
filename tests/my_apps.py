import time

from selenium.webdriver.common.by import By

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
        self.driver.get(constants.my_apps)
        time.sleep(10)
        self.driver.find_element('xpath', "//input[@name='loginfmt']").send_keys(constants.pharma_email)
        time.sleep(2)
        self.driver.find_element('xpath', "//input[@data-report-event='Signin_Submit']").click()
        time.sleep(5)
        self.driver.find_element('xpath', "//input[@name='passwd']").send_keys(constants.password1)
        time.sleep(2)
        self.driver.find_element('xpath', "//input[@data-report-event='Signin_Submit']").click()
        time.sleep(5)
        self.driver.find_element('xpath', "//input[@data-report-event='Signin_Submit']").click()
        time.sleep(10)
        #self.driver.find_element('xpath', "//*[@id='root']/div/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div[6]/div/div/div/div/div/div/a/div/img").click()
        self.driver.find_element(By.LINK_TEXT, 'DocuSign').click()
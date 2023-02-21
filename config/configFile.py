from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

my_element_id = 'something'
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
    .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))


######### HTML reports #########

# It is Hook for adding environment info to HTML reports
def pytest_configure(config):
    config._metadata['Project Name'] = 'DocuSign'
    config._metadata['Tester'] = 'Apparao Jajimoggala'


# It is Hook for delete/modify environment info to HTML report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.yield_fixture(scope="session")
def driver():
   _driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")
   return _driver


@pytest.fixture(scope="session", autouse=True)
def stop(request, driver):
   def fin():
       driver.quit()
   request.addfinalizer(fin)


driver = driver()


def filling_in_any_field(self, element, message_text):
    driver.find_element_by_xpath(element).clear()
    driver.find_element_by_xpath(element).send_keys(message_text)


def wait_for_webelement(self, element_xpath):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))


def get_current_url_page():
    wait_for_webelement()
    url = driver.current_url




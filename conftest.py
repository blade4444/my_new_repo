import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure.constants import AttachmentType
import allure, json


@pytest.yield_fixture(scope="session")
def driver():
   _driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")
   _driver.maximize_window()
   return _driver


@pytest.fixture(scope="session", autouse=True)
def stop(request, driver):
   def fin():
       driver.quit()
   request.addfinalizer(fin)


# driver = driver()

# driver.find_element_by_xpath("")

def filling_in_any_field(element, message_text):
    driver.find_element_by_xpath(element).clear()
    driver.find_element_by_xpath(element).send_keys(message_text)


def waiting_for_an_item_to_appear(element):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, element)))

def waiting_for_item_to_disappear(element):
    wait = WebDriverWait(driver, 10)
    driver.refresh()
    wait.until(EC.staleness_of(element))

def waiting_for_item_visibility(element):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of(element))

def waiting_to_change_the_attribute_value_of_an_element():
    WebDriverWait(driver, 60).until(lambda _: driver.find_element_by_name('vpn_switch').text == 'connected')

def get_current_url_page():
    waiting_for_an_item_to_appear()
    url = driver.current_url

# @pytest.fixture(scope="session", autouse=True)
# def adding_attachments():
#     with allure.MASTER_HELPER.step('Error'):
#        allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    # allure.MASTER_HELPER.attach('request body', json.dumps(params, indent=4), type=AttachmentType.JSON)
    #
    # allure.MASTER_HELPER.attach('URL', str(data.url), type=AttachmentType.TEXT)





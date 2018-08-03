from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver:
    def __init__(self, driver):
        self.driver = driver

    # driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")

    def filling_in_any_field(self, element, message_text):
        self.driver.find_element_by_xpath(element).clear()
        self.driver.find_element_by_xpath(element).send_keys(message_text)

    def waiting_for_an_item_to_appear(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, element)))

    def waiting_for_item_to_disappear(self, element):
        wait = WebDriverWait(self.driver, 10)
        self.driver.refresh()
        wait.until(EC.staleness_of(element))

    def waiting_for_item_visibility(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(element))

    def waiting_to_change_the_attribute_value_of_an_element(self):
        WebDriverWait(self.driver, 60).until(lambda _: self.driver.find_element_by_name('vpn_switch').text == 'connected')

    def get_current_url_page(self, element):
        self.waiting_for_an_item_to_appear(element=element)
        url = self.driver.current_url
        return url







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
from selenium.webdriver.common.action_chains import ActionChains


class Driver:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")

    def find_element(self, element, click_el=False, by_css_sel=False, class_name=False, by_id=False):
        self.waiting_for_an_item_to_appear(element)
        if by_css_sel:
            element_xp = self.driver.find_element_by_css_selector(element)
        elif class_name:
            element_xp = self.driver.find_element_by_class_name(element)
        elif by_id:
            element_xp = self.driver.find_element_by_id(element)
        else:
            element_xp = self.driver.find_element_by_xpath(element)
        if click_el:
            element_xp.click()
        return element_xp

    def filling_in_a_field(self, element, message_text, clear=True):
        self.waiting_for_an_item_to_appear(element)
        if clear:
            self.driver.find_element_by_xpath(element).clear()
        self.driver.find_element_by_xpath(element).send_keys(message_text)

    def waiting_for_an_item_to_appear(self, element):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))

    def waiting_for_item_to_disappear(self, element):
        self.driver.refresh()
        self.wait.until(EC.staleness_of(element))

    def waiting_for_item_visibility(self, element):
        self.wait.until(EC.visibility_of(element))

    def waiting_to_change_the_attribute_value_of_an_element(self):
        WebDriverWait(self.driver, 60).until(lambda _: self.driver.find_element_by_name('vpn_switch').text == 'connected')

    def get_current_url_page(self, element):
        self.waiting_for_an_item_to_appear(element=element)
        url = self.driver.current_url
        return url

    def hover_element_open(self, element_for_hover, waiting_for_an_element):
        element_for_hover = self.driver.find_element_by_xpath(element_for_hover)
        ActionChains(self.driver).move_to_element(element_for_hover).click_and_hold(element_for_hover).perform()
        self.waiting_for_an_item_to_appear(waiting_for_an_element)

    def get_text_from_element(self, element):
        text = self.find_element(element).text
        return text





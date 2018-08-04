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

    def divide(self, element):
        """
        We can transfer an element with a search method and a locator. For example:
        "id=hesoyam".
        Values that can be taken by_what:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        by_what, element = element[:element.find('=')], element[element.find('=') + 1:]
        return by_what, element

    def find_element_h(self, element, click_el=False):
        self.waiting_for_an_item_to_appear(element)
        by_what, element = self.divide(element)
        element_xp = self.driver.find_element(by_what, element)
        if click_el:
            element_xp.click()
        return element_xp

    def filling_in_a_field(self, element, message_text, clear=False):
        # self.waiting_for_an_item_to_appear(element)
        element = self.find_element_h(element)

        #TODO:
        if clear:
            element.clear()
        element.send_keys(message_text)

    def waiting_for_an_item_to_appear(self, element):
        by_what, element = self.divide(element)
        self.wait.until(EC.element_to_be_clickable((by_what, element)))

    # def waiting_for_item_to_disappear(self, element):
    #     self.driver.refresh()
    #     self.wait.until(EC.staleness_of(element))
    #
    # def waiting_for_item_visibility(self, element):
    #     self.wait.until(EC.visibility_of(element))
    #
    # def waiting_to_change_the_attribute_value_of_an_element(self):
    #     WebDriverWait(self.driver, 60).until(lambda _: self.driver.find_element_by_name('vpn_switch').text == 'connected')

    def get_current_url_page(self, element):
        self.waiting_for_an_item_to_appear(element=element)
        url = self.driver.current_url
        return url

    def hover_element_open(self, element_for_hover, waiting_for_an_element):
        element_for_hover = self.driver.find_element_h(element_for_hover)
        # TODO
        action = ActionChains(self.driver)
        action = action.move_to_element(element_for_hover)
        action.click_and_hold(element_for_hover).perform()
        self.waiting_for_an_item_to_appear(waiting_for_an_element)
        # ActionChains(self.driver).move_to_element(element_for_hover).click_and_hold(element_for_hover).perform()
        # self.waiting_for_an_item_to_appear(waiting_for_an_element)

    def get_text_from_element(self, element):
        text = self.find_element_h(element).text
        return text

    def into_the_iframe(self, element):
        self.driver.switch_to_frame(self.find_element_h(element))

    def exit_the_iframe(self):
        self.driver.switch_to.default_content()

    def operation_into_iframe(self, element, iframe_butt, message, el_for_message, iframe_for_mess):
        self.driver.switch_to_frame(self.find_element_h(iframe_butt))
        self.driver.find_element_by_xpath(element).click()
        self.driver.switch_to.default_content()

        self.driver.switch_to_frame(self.find_element_h(iframe_for_mess))
        self.driver.find_element_by_xpath(el_for_message).send_keys(message)

        # body_m = self.driver.find_element_by_xpath(el_for_message).send_keys(message)
        self.driver.switch_to.default_content()





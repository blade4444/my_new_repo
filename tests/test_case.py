# from selenium import webdriver
# from conftest import *
#
# # driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")
# # driver.find_element_by_xpath()
#
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
#
#
# def test_first(driver):
#     driver.get("https://www.vpnunlimitedapp.com/")
#     # driver.
#
#
#
# # import requests
# # import conftest
# #
# # user = 'alexey'
# # password = 'styagaylo'
# # base_url = 'http://httpbin.org/'
# #
# #
# # def test_my_first_api_test():
# #    r = requests.post(base_url + 'post', data={'user': user, 'password': password})
# #    assert r.status_code == 200, "Unexpected status code: {}".format(r.status_code)
# #    assert r.json()['url'] == base_url + 'post', "Unexpected url: {}".format(r.json()['url'])
# #    assert r.json()['form']['user'] == user, "Unexpected user: {}".format(r.json()['form']['user'])
# #    assert r.json()['form']['password'] == password, \
# #       "Unexpected password: {}".format(r.json()['form']['password'])
# #
# # def test_eg(driver):
# #    a = conftest.writer_message()


from page.login_page import AdminPanelLoginPage
from allure.constants import AttachmentType
import allure



def test_login_to_admin_panel(driver):

    admin_login_page = AdminPanelLoginPage(driver)

    """
    === Description:
    # Open site "http://example.com"
    # Enter username
    # Enter password
    # Submit login

    === Expected result:
    * Username should be in the title
    """

    username = "blademax1996@gmail.com"
    password = "blade80668481722"
    admin_login_page.sign_in_account(username=username, password=password)

    with allure.MASTER_HELPER.step('Error'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


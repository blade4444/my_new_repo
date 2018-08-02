from selenium import webdriver
from conftest import *

# driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")
# driver.find_element_by_xpath()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_first(driver):
    driver.get("https://www.vpnunlimitedapp.com/")
    # driver.



# import requests
# import conftest
#
# user = 'alexey'
# password = 'styagaylo'
# base_url = 'http://httpbin.org/'
#
#
# def test_my_first_api_test():
#    r = requests.post(base_url + 'post', data={'user': user, 'password': password})
#    assert r.status_code == 200, "Unexpected status code: {}".format(r.status_code)
#    assert r.json()['url'] == base_url + 'post', "Unexpected url: {}".format(r.json()['url'])
#    assert r.json()['form']['user'] == user, "Unexpected user: {}".format(r.json()['form']['user'])
#    assert r.json()['form']['password'] == password, \
#       "Unexpected password: {}".format(r.json()['form']['password'])
#
# def test_eg(driver):
#    a = conftest.writer_message()

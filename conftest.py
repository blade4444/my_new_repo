import pytest, data
from selenium import webdriver


@pytest.yield_fixture(scope="session")
def driver():
    _driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")
    _driver.maximize_window()
    _driver.get(data.web_site_main)
    return _driver


@pytest.fixture(scope="session", autouse=True)
def stop(request, driver):
    def fin():
        driver.quit()
    request.addfinalizer(fin)




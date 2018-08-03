from page.login_page import AdminPanelLoginPage
from allure.constants import AttachmentType
import allure


def test_login(driver):
    """
    === Description:
    # Open site "http://example.com"
    # Enter username
    # Enter password
    # Submit login

    === Expected result:
    * Username should be in the title
    """
    login_page = AdminPanelLoginPage(driver)
    login_page.open_url()
    login_page.sign_in_account()

    login_page.verify_sign_in_account()

    with allure.MASTER_HELPER.step('Error'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


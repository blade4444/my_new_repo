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
    # Verify login

    === Expected result:
    * Username should be in the title
    """
    main_page = AdminPanelLoginPage(driver)
    main_page.sign_in_account()
    main_page.verify_sign_in_account()
    with allure.MASTER_HELPER.step('Error'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)



def test_logout(driver):
    '''
    === Description:
    # Push the button Sign out
    # Verify logout
    === Expected result:
    * Sign in should be in the title
    '''
    main_page = AdminPanelLoginPage(driver)
    main_page.verify_sign_out()
    with allure.MASTER_HELPER.step('Error'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
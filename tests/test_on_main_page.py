from page.main_page import MainPage
from allure.constants import AttachmentType
import allure


# def test_01_login(driver):
#     """
#     === Description:
#     # Open site "http://example.com"
#     # Enter username
#     # Enter password
#     # Submit login
#     # Verify login
#
#     === Expected result:
#     * Username should be in the title
#     """
#     main_page = MainPage(driver)
#     main_page.sign_in_account()
#     main_page.verify_sign_in_account()
#     with allure.MASTER_HELPER.step('test_01_login'):
#      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
#
#
# def test_02_logout(driver):
#     """
#     === Description:
#     # Push the button Sign out
#     # Verify logout
#     === Expected result:
#     * Sign in should be in the title
#     """
#     main_page = MainPage(driver)
#     main_page.verify_sign_out()
#     with allure.MASTER_HELPER.step('test_02_logout'):
#      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
#

# def test_03_checking_work_logo_button(driver):
#     """
#     === Description:
#     # Go to any tab in the menu bar
#     # Return with the logo
#
#     === Expected result:
#     * Pressing the logo button will return to the main page
#     """
#     main_page = MainPage(driver)
#     main_page.rand_transition_between_header_menu()
#     main_page.verify_working_logo_button()
#     with allure.MASTER_HELPER.step('test_03_checking_work_logo_button'):
#      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


# def test_04_send_message_to_support(driver):
#
#     main_page = MainPage(driver)
#     main_page.open_support_window()
#     main_page.write_message_to_support()
#     main_page.send_mesage_to_support()
#     with allure.MASTER_HELPER.step('test_04_send_message_to_support'):
#       allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
from page.main_page import MainPage
from allure.constants import AttachmentType
import allure


def test_01_login(driver):
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
    main_page = MainPage(driver)
    main_page.sign_in_account()
    with allure.MASTER_HELPER.step('test_01_login'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.verify_sign_in_account()
    with allure.MASTER_HELPER.step('test_01_login'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


def test_02_logout(driver):
    """
    === Description:
    # Push the button Sign out
    # Verify logout
    === Expected result:
    * Sign in should be in the title
    """
    main_page = MainPage(driver)
    main_page.verify_sign_out()
    with allure.MASTER_HELPER.step('test_02_logout'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


# def test_03_send_message_to_support(driver):
#     """
#     === Description:
#     # Open support window in the right down corner
#     # Input in the field correct data
#     # Click button 'Send'
#     === Expected result:
#     * The message will be sent
#     """
#     main_page = MainPage(driver)
#     main_page.open_support_window()
#     with allure.MASTER_HELPER.step('test_03_send_message_to_support'):
#       allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
#     main_page.write_message_to_support()
#     with allure.MASTER_HELPER.step('test_03_send_message_to_support'):
#       allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
#     main_page.send_message_to_support()
#     with allure.MASTER_HELPER.step('test_03_send_message_to_support'):
#       allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


def test_04_checking_work_logo_button(driver):
    """
    === Description:
    # Go to any tab in the menu bar
    # Return with the logo

    === Expected result:
    * Pressing the logo button will return to the main page
    """
    main_page = MainPage(driver)
    main_page.rand_transition_between_header_menu()
    with allure.MASTER_HELPER.step('test_04_checking_work_logo_button'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.verify_working_logo_button()
    with allure.MASTER_HELPER.step('test_04_checking_work_logo_button'):
     allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


def test_05_negative_send_message_to_support_with_incorrect_email(driver):
    """
    === Description:
    # Open support window in the right down corner
    # Input in the field incorrect data
    === Expected result:
    * Button 'Send' is disabled
    * The message will not be sent
    """
    main_page = MainPage(driver)
    main_page.open_support_window()
    with allure.MASTER_HELPER.step('test_05_negative_send_message_to_support_with_incorrect_email'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.write_message_to_support(negative=True)
    with allure.MASTER_HELPER.step('test_05_negative_send_message_to_support_with_incorrect_email'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.verify_button_send_message_to_supp_is_disabled()
    with allure.MASTER_HELPER.step('test_05_negative_send_message_to_support_with_incorrect_email'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


def test_06_verify_subscribe_to_us_positive(driver):
    """
    === Description:
    # In the form "Subscribe to us" incert correct email
    # Click button for subscriber
    === Expected result:
    * Subscription will be successful
    """
    main_page = MainPage(driver)
    main_page.input_data_in_subscriber_to_us_field()
    with allure.MASTER_HELPER.step('test_05_negative_send_message_to_support_with_incorrect_email'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.send_email_for_subscribe()
    with allure.MASTER_HELPER.step('test_05_negative_send_message_to_support_with_incorrect_email'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.verify_subscriber_operation()
    with allure.MASTER_HELPER.step('test_06_verify_subscribe_to_us_positive'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


def test_07_verify_subscribe_to_us_negative(driver):
    """
    === Description:
    # In the form "Subscribe to us" incert incorrect email
    # Click button for subscriber
    === Expected result:
    * Subscription will not be successful
    """
    main_page = MainPage(driver)
    main_page.input_data_in_subscriber_to_us_field(positive=False)
    with allure.MASTER_HELPER.step('test_05_negative_send_message_to_support_with_incorrect_email'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.send_email_for_subscribe()
    with allure.MASTER_HELPER.step('test_07_verify_subscribe_to_us_negative'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    main_page.verify_subscriber_operation(positive=False)



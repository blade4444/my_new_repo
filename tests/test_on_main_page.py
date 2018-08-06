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
    main_page.get_screen_shot("test_01_login")
    main_page.verify_sign_in_account()
    main_page.get_screen_shot("test_01_login")



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
    main_page.get_screen_shot("test_02_logout")


def test_03_send_message_to_support(driver):
    """
    #=== Description:
    # Open support window in the right down corner
    # Input in the field correct data
    # Click button 'Send'
    #=== Expected result:
    #* The message will be sent
    """
    main_page = MainPage(driver)
    main_page.open_support_window()
    main_page.get_screen_shot("test_03_send_message_to_support")
    main_page.write_message_to_support()
    main_page.get_screen_shot("test_03_send_message_to_support")
    main_page.send_message_to_support()
    main_page.get_screen_shot("test_03_send_message_to_support")
    main_page.verify_send_message_is_successful()


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
    main_page.get_screen_shot("test_04_checking_work_logo_button")
    main_page.verify_working_logo_button()
    main_page.get_screen_shot("test_04_checking_work_logo_button")


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
    main_page.get_screen_shot("test_05_negative_send_message_to_support_with_incorrect_email")
    main_page.write_message_to_support(negative=True)
    main_page.get_screen_shot("test_05_negative_send_message_to_support_with_incorrect_email")
    main_page.verify_button_send_message_to_supp_is_disabled()
    main_page.get_screen_shot("test_05_negative_send_message_to_support_with_incorrect_email")


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
    main_page.send_email_for_subscribe()
    main_page.get_screen_shot("test_06_verify_subscribe_to_us_positive")
    main_page.verify_subscriber_operation()
    main_page.get_screen_shot("test_06_verify_subscribe_to_us_positive")
    main_page.close_information_window_with_subscriber()

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
    main_page.get_screen_shot("test_07_verify_subscribe_to_us_negative")
    main_page.send_email_for_subscribe()
    main_page.get_screen_shot("test_07_verify_subscribe_to_us_negative")
    main_page.verify_subscriber_operation(positive=False)
    main_page.get_screen_shot("test_07_verify_subscribe_to_us_negative")
    main_page.close_information_window_with_subscriber()



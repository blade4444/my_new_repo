from page.login_page import AdminPanelLoginPage
from allure.constants import AttachmentType
import allure


def test_login_to_admin_panel(driver):
   """
   === Description:
   # Open site "http://example.com"
   # Enter username
   # Enter password
   # Submit login

   === Expected result:
   * Username should be in the title
   """
   admin_panel = AdminPanelLoginPage(driver)
   admin_panel.open()
   admin_panel.enter_username("blademax1996@gmail.com")
   admin_panel.enter_password("blade80668481722")
   admin_panel.submit_login()


   with allure.MASTER_HELPER.step('Error'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)


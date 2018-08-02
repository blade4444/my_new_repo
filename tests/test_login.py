from page.login_page import AdminPanelLoginPage

username = "username"
password = "password"

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
   admin_panel.enter_username(username)
   admin_panel.enter_password(password)
   admin_panel.submit_login()
   assert username in driver.title

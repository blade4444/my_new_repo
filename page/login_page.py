class AdminPanelLoginPage:

   def __init__(self, driver):
       self.driver = driver

   def open(self):
       self.driver.get("http://example.com")
       return self

   def enter_username(self, username):
       self.driver.find_element_by_name("username").send_keys(username)
       return self

   def enter_password(self, password):
       self.driver.find_element_by_name("password").send_keys(password)
       return self

   def submit_login(self):
       self.driver.find_element_by_name("login").click()
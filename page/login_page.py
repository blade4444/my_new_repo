import conftest

class AdminPanelLoginPage:

    input_email_xpath = "//h4[text()='Email (KeepSolid ID)']/ancestor::div[@class='user_login']/descendant::input"
    input_password_xpath = "//h4[text()='Password']/ancestor::div[@class='log_sec_input_cnt left_tab tab-content active-tab']" \
                     "/descendant::div[@class='user_pass']/descendant::input"
    login_xpath = "//button[@class='l_s_login_btn button-find' and text()='Login']"
    my_acc_veryfy_xpath = "//li//a[text()='My account']"
    info_window_email_xp = "//div[@class='h_user_info_wrapper']//span[text()='blademax1996@gmail.com']"

    def __init__(self, driver):
        self.driver = driver

    def sign_in_account(self, username, password):
        self.driver.get("https://www.vpnunlimitedapp.com/en")
        self.driver.find_element_by_xpath("//li//a[text()='Sign In']").click()
        self.driver.find_element_by_xpath(self.input_email_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.input_password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.login_xpath).click()

        conftest.waiting_for_an_item_to_appear(element=self.my_acc_veryfy_xpath)
        self.my_acc_veryfy_xpath.click()
        expected_name_user = self.driver.find_element_by_xpath(self.info_window_email_xp).text
        assert expected_name_user == username, ("Expected username %s is not actual username %s") % expected_name_user \
                                               % username


   #  def open(self):
   #     self.driver.get("https://www.vpnunlimitedapp.com/en")
   #     return self
   #
   # def enter_username(self, username):
   #     self.driver.find_element_by_xpath("//li//a[text()='Sign In']").send_keys(username)
   #     self.driver
   #     return self
   #
   # def enter_password(self, password):
   #     self.driver.find_element_by_name("password").send_keys(password)
   #     return self
   #
   # def submit_login(self):
   #     self.driver.find_element_by_name("login").click()
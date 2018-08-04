from helpers import Driver
import data


class AdminPanelLoginPage:

    sign_in_button = "//li//a[text()='Sign In']"
    input_email_xpath = "//h4[text()='Email (KeepSolid ID)']/ancestor::div[@class='user_login']/descendant::input"
    input_password_xpath = "//h4[text()='Password']/ancestor::div[@class='log_sec_input_cnt left_tab tab-content active-tab']" \
                     "/descendant::div[@class='user_pass']/descendant::input"
    login_button_xpath = "//button[@class='l_s_login_btn button-find' and text()='Login']"
    my_acc_button_xpath = "//li//a[text()='My account']"
    info_window_email_xp = "//div[@class='h_user_info_wrapper']//span[@class='h_user_mail']"
    el_hover_change_xp = "//*[@class='nav_sol_par user_prof_menu hovered']"
    log_out_button_xp = "//*[@class='h_user_logout icon-font-logout']"

    def __init__(self, driver):
        self.driver = driver
        self.driver_h = Driver(driver)

    # def open_url(self):
    #     self.driver.get(data.web_site_main)

    def sign_in_account(self, username=data.username, password=data.password):
        self.driver_h.find_element(element=self.sign_in_button, click_el=True)
        self.driver_h.filling_in_a_field(element=self.input_email_xpath, message_text=username)
        self.driver_h.filling_in_a_field(element=self.input_password_xpath, message_text=password)
        self.driver_h.find_element(element=self.login_button_xpath, click_el=True)
        self.driver_h.waiting_for_an_item_to_appear(element=self.my_acc_button_xpath)

    def verify_sign_in_account(self):
        self.driver_h.hover_element_open(self.my_acc_button_xpath, self.el_hover_change_xp)
        actual_name_user = self.driver_h.get_text_from_element(self.info_window_email_xp)
        assert actual_name_user == data.username, ("Expected username %s is not actual username %s") \
                                               % actual_name_user % data.username

    def verify_sign_out(self):
        self.driver_h.hover_element_open(self.my_acc_button_xpath, self.el_hover_change_xp)
        self.driver_h.find_element(click_el=True, element=self.log_out_button_xp)
        actual_title = self.driver_h.get_text_from_element(self.sign_in_button)
        assert actual_title == "SIGN IN", ("Expected title 'Sign In' is not actual username %s") % actual_title


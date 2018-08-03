from base_page import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class AdminPanelLoginPage:

    web_site = "https://www.vpnunlimitedapp.com/en"
    input_email_xpath = "//h4[text()='Email (KeepSolid ID)']/ancestor::div[@class='user_login']/descendant::input"
    input_password_xpath = "//h4[text()='Password']/ancestor::div[@class='log_sec_input_cnt left_tab tab-content active-tab']" \
                     "/descendant::div[@class='user_pass']/descendant::input"
    login_xpath = "//button[@class='l_s_login_btn button-find' and text()='Login']"
    my_acc_veryfy_xpath = "//li//a[text()='My account']"
    info_window_email_xp = "//div[@class='h_user_info_wrapper']//span[@class='h_user_mail']"
    el_hover_xp = "//*[@class='nav_sol_par user_prof_menu hovered']"

    def __init__(self, driver):
        self.driver = driver
        self.baseclass = Driver(driver)

    # driver = webdriver.Chrome("/home/blade/PycharmProjects/my_new_repo/chromedriver")
    # baseclass = Driver()

    def sign_in_account(self, username, password):

        self.driver.get(self.web_site)
        self.driver.find_element_by_xpath("//li//a[text()='Sign In']").click()
        self.driver.find_element_by_xpath(self.input_email_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.input_password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.login_xpath).click()

        self.baseclass.waiting_for_an_item_to_appear(element=self.my_acc_veryfy_xpath)
        element_to_hover = self.driver.find_element_by_xpath(self.my_acc_veryfy_xpath)
        ActionChains(self.driver).move_to_element(element_to_hover).perform()

        self.baseclass.waiting_for_an_item_to_appear(self.el_hover_xp)
        expected_name_user = self.driver.find_element_by_xpath(self.info_window_email_xp).text

        assert expected_name_user == username, ("Expected username %s is not actual username %s") \
                                               % expected_name_user % username



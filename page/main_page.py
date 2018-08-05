from helpers import Driver
import data, random, traceback


class MainPage:

    sign_in_button = "xpath=//li//a[text()='Sign In']"
    input_email_xpath = "xpath=//h4[text()='Email (KeepSolid ID)']/ancestor::div[@class='user_login']/descendant::input"
    input_password_xpath = "xpath=//h4[text()='Password']/ancestor::div[@class='log_sec_input_cnt left_tab tab-content active-tab']" \
                     "/descendant::div[@class='user_pass']/descendant::input"
    login_button_xpath = "xpath=//button[@class='l_s_login_btn button-find' and text()='Login']"
    my_acc_button_xpath = "xpath=//li//a[text()='My account']"
    info_in_my_acc_hover = "xpath=//div[@class='h_user_info_wrapper']//span[@class='h_user_mail']"
    el_hover_change_xp = "xpath=//*[@class='nav_sol_par user_prof_menu hovered']"
    log_out_button_xp = "xpath=//a[@class='h_user_logout icon-font-logout']"
    extras_button_xp = "xpath=//a[@class='drop_item ' and text()='Extras']"
    pricing_button_xp = "xpath=//div[@class='navbar-wrap']//a[@class=' pricing--special--link']"
    downloads_button_xp = "xpath=//div[@class='navbar-wrap']//a[text()='Downloads']"
    info_button_xp = "xpath=//div[@class='navbar-wrap']//a[text()='Info']"
    support_button_xp = "xpath=//div[@class='navbar-wrap']//a[text()='Support']"
    blog_button_xp = "xpath=//div[@class='navbar-wrap']//a[text()='Blog']"
    logo_button_xp = "xpath=//a[@class='navbar-brand']"
    video_play_button_xp = "xpath=//div[@class='pulse2']"
    get_this_deal_button = "xpath=//div[@class='wrapper_button']//a"
    actual_url_page = "xpath=//link[@href and @rel='canonical']"

    ################################################ xpath for send message to support ############################
    supp_butt_in_right_bottom = "xpath=//*[@class='src-component-Launcher-label Arrange-sizeFit u-textInheritColor u-inlineBlock ']"
    input_name_xp = "xpath=//input[@name='name']"
    input_email_xp = "xpath=//div[@id='Embed']//input[@name='email']"
    input_message_xp = "xpath=//div[@id='Embed']//*[@name='description']"
    send_message_button_xp = "xpath=//div[@id='Embed']//*[@type='submit' and @value]"
    send_message_successful_butt_xp = "xpath=//div[@id='Embed']//input[@type='button']"
    in_iframe_button_xp = "xpath=//iframe[@id='launcher']"
    iframe_for_into_the_window = "id=webWidget"



    def __init__(self, driver):
        self.driver_h = Driver(driver)

    def sign_in_account(self, username=data.username, password=data.password):
        self.driver_h.find_element_h(element=self.sign_in_button, click_el=True)
        self.driver_h.filling_in_a_field(element=self.input_email_xpath, message_text=username)
        self.driver_h.filling_in_a_field(element=self.input_password_xpath, message_text=password)
        self.driver_h.find_element_h(element=self.login_button_xpath, click_el=True)
        self.driver_h.waiting_for_an_item_to_appear(element=self.my_acc_button_xpath)

    def verify_sign_in_account(self):
        self.driver_h.hover_element_open(self.my_acc_button_xpath)
        actual_name_user = self.driver_h.get_text_from_element(self.info_in_my_acc_hover)
        assert actual_name_user == data.username, ("Expected username %s is not actual username %s") \
                                               % actual_name_user % data.username

    def verify_sign_out(self):
        self.driver_h.hover_element_open(self.my_acc_button_xpath)
        self.driver_h.find_element_h(click_el=True, element=self.log_out_button_xp)
        actual_title = self.driver_h.get_text_from_element(self.sign_in_button)
        assert actual_title == "SIGN IN", ("Expected title 'Sign In' is not actual username %s") % actual_title

    def rand_transition_between_header_menu(self):
        element = random.choice([self.extras_button_xp, self.info_button_xp, self.support_button_xp,
                                 self.pricing_button_xp, self.downloads_button_xp, self.blog_button_xp])
        self.driver_h.find_element_h(element=element, click_el=True)

    def verify_working_logo_button(self):
        self.driver_h.find_element_h(self.logo_button_xp, click_el=True)
        actual_url = self.driver_h.get_attribute_element(element=self.actual_url_page, attribute="href")
        assert actual_url == data.web_site_main, ("Expected url %s is not actual username %s") % data.web_site_main\
                                                 % actual_url

    def open_support_window(self):
        self.driver_h.into_the_iframe(element=self.in_iframe_button_xp)
        self.driver_h.find_element_h(element=self.supp_butt_in_right_bottom, click_el=True)
        self.driver_h.exit_the_iframe()

    def write_message_to_support(self, negative=False):
        self.driver_h.into_the_iframe(element=self.iframe_for_into_the_window)
        self.driver_h.filling_in_a_field(element=self.input_name_xp, message_text=data.name)
        self.driver_h.filling_in_a_field(element=self.input_email_xp,
                                         message_text=random.choice(data.negative_email) if negative else data.email)
        self.driver_h.filling_in_a_field(element=self.input_message_xp, message_text=data.message)

    def send_message_to_support(self):
        self.driver_h.find_element_h(element=self.send_message_button_xp, click_el=True)
        try:
            self.driver_h.find_element_h(element=self.send_message_successful_butt_xp, click_el=True)
        except Exception as err:
            raise Exception("###########################################################################\n"
                  "Error: Message was not send\n")
        finally:
            self.driver_h.exit_the_iframe()

    def verify_button_send_message_to_supp_is_disabled(self):
        value_elements = self.driver_h.verify_element_is_enabled_or_disabled(self.send_message_button_xp)
        assert value_elements == "true", ("Send button is enabled whith incorect email!")
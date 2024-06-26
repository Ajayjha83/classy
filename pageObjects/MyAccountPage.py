from selenium.webdriver.common.by import By

class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    textbox_email_xpath = "//input[@name='username']"
    password_input_xpath = "//input[@name='password']"
    login_button_xpath = "//button[text()='Log in']"
    remember_me_checkbox_xpath = "//input[@name='rememberme']"
    lost_password_link_xpath = "//a[text()='Lost your password?']"
    register_phone_input_xpath = "//input[@name='reg_phone']"
    register_username_input_xpath = "//input[@name='reg_username']"
    register_email_input_xpath = "//input[@name='reg_email']"
    register_password_input_xpath = "//input[@name='reg_password']"
    register_button_xpath = "//button[text()='Register']"
    terms_conditions_checkbox_xpath = "//input[@name='terms']"
    terms_conditions_link_xpath = "//a[text()='terms & conditions']"

    # Actions
    def click_logo(self):
        self.driver.find_element(By.XPATH, self.logo_xpath).click()

    def search(self, query):
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()

    def click_cart_icon(self):
        self.driver.find_element(By.XPATH, self.cart_icon_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_link_xpath).click()

    def click_wishlist(self):
        self.driver.find_element(By.XPATH, self.wishlist_link_xpath).click()

    def enter_phone_or_email(self, phone_email):
        input_field = self.driver.find_element(By.XPATH, self.phone_email_input_xpath)
        input_field.clear()
        input_field.send_keys(phone_email)

    def enter_password(self, password):
        input_field = self.driver.find_element(By.XPATH, self.password_input_xpath)
        input_field.clear()
        input_field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_remember_me(self):
        self.driver.find_element(By.XPATH, self.remember_me_checkbox_xpath).click()

    def click_lost_password(self):
        self.driver.find_element(By.XPATH, self.lost_password_link_xpath).click()

    def enter_register_phone(self, phone):
        input_field = self.driver.find_element(By.XPATH, self.register_phone_input_xpath)
        input_field.clear()
        input_field.send_keys(phone)

    def enter_register_username(self, username):
        input_field = self.driver.find_element(By.XPATH, self.register_username_input_xpath)
        input_field.clear()
        input_field.send_keys(username)

    def enter_register_email(self, email):
        input_field = self.driver.find_element(By.XPATH, self.register_email_input_xpath)
        input_field.clear()
        input_field.send_keys(email)

    def enter_register_password(self, password):
        input_field = self.driver.find_element(By.XPATH, self.register_password_input_xpath)
        input_field.clear()
        input_field.send_keys(password)

    def click_register_button(self):
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()

    def check_terms_conditions(self):
        self.driver.find_element(By.XPATH, self.terms_conditions_checkbox_xpath).click()

    def click_terms_conditions_link(self):
        self.driver.find_element(By.XPATH, self.terms_conditions_link_xpath).click()

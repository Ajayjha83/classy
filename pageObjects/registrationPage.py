from selenium.webdriver.common.by import By


class RegistrationPage:


    # Locators
    textbox_mobile_xpath = "//form[@class='woocommerce-form woocommerce-form-register register']//input[@name='xoo-ml-reg-phone']"
    textbox_Username_xpath = "//input[@id='reg_username']"
    textbox_emailid_id = "id='reg_email'"
    textbox_password_id = "reg_password"
    checkbox_terms_id = "terms"
    button_register_xpath = "button[value='Register']"
    button_login_with_email_password_xpath = "//button[normalize-space()='Login with Email & Password']"
    textbox_phone_no_or_email_address = "//input[@id='username']"
    textbox_password_for_logi_xpath = "// input[ @ id = 'password']"
    button_login_xpath = "//button[text()='Log in']"
    text_login_varification_login_xath = "//strong[1]"


    def __init__(self, driver):
        self.driver = driver

    # Actions method
    def set_mobile_no(self,mobileno):
        self.driver.find_element(By.XPATH, self.textbox_mobile_xpath).send_keys(mobileno)

    def set_usermame(self,username):
        self.driver.find_element(By.XPATH, self.textbox_Username_xpath).send_keys(username)

    def set_emailid(self,emailid):
        self.driver.find_element(By.ID, self.textbox_emailid_id).send_keys(emailid)

    def set_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def set_tern(self):
        self.driver.find_element(By.ID, "terms").click()

    def click_Registre(self):
        self.driver.find_element(By.XPATH,self.button_register_xpath).click()
        return self.driver_find_element(By.XPATH,self.test_confmessage_xpath).text

    def click_login_with_email_and_password_button(self):
        self.driver.find_element(By.XPATH, self.button_login_with_email_password_xpath).click()

    def set_email_or_password_for_login(self,username):
        self.driver.find_element(By.XPATH,self.textbox_phone_no_or_email_address).send_keys(username)

    def set_password_for_login(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_for_logi_xpath).send_keys(password)

    def click_login_button_for_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def login_varification_test(self):
        verificaton_text = self.driver.find_element(By.XPATH, self.text_login_varification_login_xath).text
        return verificaton_text


import logging
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Importing ChromeDriverManager
from pageObjects.homePage import HomePage
from pageObjects.registrationPage import RegistrationPage
from utilities.readProperty import Readconfig
from utilities.customLogger import LogGen


class Test_Login_001:

    baseURL = Readconfig.get_application_url()
    userEmail = Readconfig.get_login_email()
    userPassword = Readconfig.get_login_password()
    logger = LogGen.loggen()

    def test_login_valid_credentials(self,setup):
        self.logger.debug("gdddddd")
        self.driver = setup       #Assign setup to the instance variable self.driver
        self.driver.get(self.baseURL)

        self.logger.info("maximize page")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.hp.click_signin()
        self.rp = RegistrationPage(self.driver)
        self.rp.click_login_with_email_and_password_button()
        self.logger.debug("$$$$Clicked on login with email and password$$$$$$$$$")
        #self.rp.set_email_or_password_for_login("ajayjha.ap@gmail.com")
        self.rp.set_email_or_password_for_login(self.userEmail)
        #self.rp.set_email_or_password_for_login(self.get_login_email)
        self.rp.set_password_for_login(self.userPassword)
        #self.rp.set_password_for_login("Ajayjha@123")
        self.rp.click_login_button_for_login()
        self.msg = self.rp.login_varification_test()
        print(self.msg)
        if self.msg == "Ajay":
            assert True
        else:
            assert False
        self.driver.close()











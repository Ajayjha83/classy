import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  #Importing ChromeDriverManager
from pageObjects.homePage import HomePage
from pageObjects.registrationPage import RegistrationPage


class Test_registration_001:
    baseURL = "https://www.classyclix.com/"


    def test_registration_flow(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.hp.click_signin()
        self.rp = RegistrationPage(self.driver)
        self.rp.set_mobile_no(9560653870)
        self.rp.set_usermame("Ajay")
        #self.rp.set_emailid("aaa@gmail.com")
        self.rp.set_password("Ananya@123")
        self.rp.set_tern()
        #mess = self.rp.click_Registre()
        #assert mess == "ddd"
        self.driver.quit()





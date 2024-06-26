from selenium.webdriver.common.by import By


class HomePage:


    # Locators

    link_logo_css = "a.navbar-brand"
    search_box_xpath = "//input[@name='search']"
    button_SignIn_linktext = "Sign In"

    # Navigation Links
    all_nav_bar_common_xpath= "(//ul[@id='menu-main-menu'])/li/a"
    # Earrings
    tab_Earrings_xpath = "(//a[@class='sf-with-ul'])[1]"
    tab_Necklaces_xpath = "(//a[@class='sf-with-ul'])[2]"
    tab_Rings_xpath = "//a[text()='Rings']"
    tab_Bracelets_xpath = "//li[@id='menu-item-2448']//a[normalize-space()='Bracelets']"
    tab_Bangles_xpath = "//li[@id='menu-item-2447']//a[normalize-space()='Bangles']"


    # Footer Links
    about_us_link_xpath = "//a[text()='About Us']"
    contact_us_link_xpath = "//a[text()='Contact us']"
    shipping_policy_link_xpath = "//a[text()='Shipping Policy']"
    return_policy_link_xpath = "//a[text()='Return Policy']"
    privacy_policy_link_xpath = "//a[text()='Privacy Policy']"
    terms_conditions_link_xpath = "//a[text()='Terms and Conditions']"

    def __init__(self, driver):
        self.driver = driver

    # Actions
    def click_logo(self):
        self.driver.find_element(By.XPATH, self.link_logo_xpath).click()

    def search(self, query):
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()

    def click_signin(self):
        self.driver.find_element(By.LINK_TEXT, self.button_SignIn_linktext).click()

    def click_wishlist(self):
        self.driver.find_element(By.XPATH, self.wishlist_link_xpath).click()

    def click_earrings(self):
        self.driver.find_element(By.XPATH, self.earrings_link_xpath).click()

    def click_necklaces(self):
        self.driver.find_element(By.XPATH, self.necklaces_link_xpath).click()

    def click_rings(self):
        self.driver.find_element(By.XPATH, self.rings_link_xpath).click()

    def click_bracelets(self):
        self.driver.find_element(By.XPATH, self.bracelets_link_xpath).click()

    def click_bangles(self):
        self.driver.find_element(By.XPATH, self.bangles_link_xpath).click()

    def click_about_us(self):
        self.driver.find_element(By.XPATH, self.about_us_link_xpath).click()

    def click_contact_us(self):
        self.driver.find_element(By.XPATH, self.contact_us_link_xpath).click()

    def click_shipping_policy(self):
        self.driver.find_element(By.XPATH, self.shipping_policy_link_xpath).click()

    def click_return_policy(self):
        self.driver.find_element(By.XPATH, self.return_policy_link_xpath).click()

    def click_privacy_policy(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_link_xpath).click()

    def click_terms_conditions(self):
        self.driver.find_element(By.XPATH, self.terms_conditions_link_xpath).click()

    def find_nav_bar_links(self):
        list_nav_bar_elements = self.driver.find_elements(By.XPATH,self.all_nav_bar_common_xpath)
        list_navbar_urls = []
        for element in list_nav_bar_elements:
            url=element.get_attribute("href")
            list_navbar_urls.append(url)
        return list_navbar_urls





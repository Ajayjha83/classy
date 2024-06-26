# locater
from selenium.webdriver.common.by import By

tab_Earrings_xpath = "(//a[@class='sf-with-ul'])[1]"

tab_Earrings_xpath = "(//a[@class='sf-with-ul'])[1]"
all_nav_bar_common_xpath = "(//ul[@id='menu-main-menu'])/li/a"
tab_Necklaces_xpath = "(//a[@class='sf-with-ul'])[2]"
tab_Rings_xpath = "//a[text()='Rings']"
tab_Bracelets_xpath = "//li[@id='menu-item-2448']//a[normalize-space()='Bracelets']"
tab_Bangles_xpath = "//li[@id='menu-item-2447']//a[normalize-space()='Bangles']"
h1_Earrings_text_xpath= "//h1[@class='entry-title']"


def __init__ (self,driver):
    self.driver = driver
tab_commant_xpath = driver.find_elements(By,*(//ul[@id='menu-main-menu'])/li/a[1])
print(tab_commant_xpath)


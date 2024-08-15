
import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.by import By


class Test_homePage_navBar_earrings:
    driver = webdriver.Chrome()
    driver.get("https://www.classyclix.com/")
    driver.maximize_window()
    driver.implicitly_wait(15)
    element_earring_tab = driver.find_element(By.XPATH,"(//a[@class='sf-with-ul' ])[1]")
    ActionChains(driver).move_to_element(element_earring_tab).perform()
    elements_all_sub_teb_under_earrings = driver.find_elements(By.XPATH,"//li[@id='menu-item-2449']/ul/li/a")

    def test_find_sub_menu_links_under_earring_tab(self):
        sub_elements = self.elements_all_sub_teb_under_earrings
        all_sub_menu_links = []
        for sub_menu in sub_elements:
            submenu = sub_menu.get_attribute('href')
            all_sub_menu_links.append(submenu)
        return all_sub_menu_links
    # now i want click on all


sub_nev_bar_instance = Test_homePage_navBar_earrings.test_find_sub_menu_links_under_earring_tab()

expected_list_of_pagetitle = []
for i in sub_nev_bar_instance:
    self.driver.get(i)
    expected_list_of_pagetitle.append(driver.title)
    print(expected_list_of_pagetitle)
actual_page_titles = ['Buy Ethnic Earrings for Women Online in India | ClassyClix',
                          'Western Archives - Classy Clix',
                          'Buy Artificial Jhumka Earrings for Women Online in India | ClassyClix',
                          'Stud Archives - Classy Clix',
                          'American Diamond Archives - Classy Clix',
                          'Buy Oxidised Jhumka Earrings for Women Online | ClassyClix',
                          'Temple Archives - Classy Clix',
                          'Buy Artificial Kundan Earrings Online in India | ClassyClix',
                          'Buy Meenakari Earrings for Women Online | ClassyClix',
                          'Under 100 Archives - Classy Clix']

if set(expected_list_of_pagetitle) == set(actual_page_titles):
    assert True
else:
    assert False
self.driver.close()

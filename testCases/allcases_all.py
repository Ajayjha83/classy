
import time
from telnetlib import EC

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.classyclix.com/")
driver.maximize_window()
element_earring_tab=driver.find_element(By.XPATH,"(//a[@class='sf-with-ul' ])[1]")
ActionChains(driver).move_to_element(element_earring_tab).perform()
elements_all_sub_teb_under_earrings = driver.find_elements(By.XPATH,"//li[@id='menu-item-2449']/ul/li/a")
def find_sub_menu_links_under_earring_tab():
    list_all_sub_menu_links=[]
    for sub_menu in elements_all_sub_teb_under_earrings:
        submenu = sub_menu.get_attribute('href')
        list_all_sub_menu_links.append(submenu)
    return list_all_sub_menu_links
# now i want click on all


list_all_sub_menu_links = find_sub_menu_links_under_earring_tab()
expected_list_of_pagetitle = []
for i in list_all_sub_menu_links:
    time.sleep(14)
    driver.get(i)
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

driver.quit()


# ###############neclaces#############

import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.classyclix.com/")
driver.maximize_window()
element_neclaces_tab=driver.find_element(By.XPATH,"//li[@id='menu-item-3354']")
ActionChains(driver).move_to_element(element_neclaces_tab).perform()
elements_all_sub_teb_under_earrings = driver.find_elements(By.XPATH,"//li[@id='menu-item-2450']/ul/li/a")
def find_sub_menu_links_under_neclaces_tab():
    list_all_sub_menu_links=[]
    for sub_menu in elements_all_sub_teb_under_earrings:
        submenu = sub_menu.get_attribute('href')
        list_all_sub_menu_links.append(submenu)
    return list_all_sub_menu_links
# now i want click on all


list_all_sub_menu_links = find_sub_menu_links_under_neclaces_tab()
expected_list_of_pagetitle = []

for i in list_all_sub_menu_links:
    driver.get(i)
    expected_list_of_pagetitle.append(driver.title)
print(expected_list_of_pagetitle)

actual_page_titles = ['American Diamond Set Archives - Classy Clix',
                              'oxidised set Archives - Classy Clix',
                              'Temple Set Archives - Classy Clix',
                              'Ethnic Archives - Classy Clix',
                              'Western Archives - Classy Clix']

if set(expected_list_of_pagetitle) == set(actual_page_titles):
    assert True
else:
    assert False

driver.quit()

# ##############check all links on home page############
import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.classyclix.com/")
driver.maximize_window()
driver.implicitly_wait(10)
all_url_elements = driver.find_elements(By.TAG_NAME,"a")
all_url = []
for i in all_url_elements:
    url = i.get_attribute('href')
    all_url.append(url)
print(all_url)

driver.close()

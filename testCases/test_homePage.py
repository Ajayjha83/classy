
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from utilities.customLogger import LogGen
from pageObjects.homePage import HomePage


class Test_homePage:
    logger = LogGen.loggen()

    def test_verify_top_nav_bar_links(self,setup):
        driver = setup
        driver.get("https://www.classyclix.com/")
        driver.maximize_window()
        driver.implicitly_wait(50)
        expected_list_nav_urls = ['https://www.classyclix.com/artificial-earrings/', 'https://www.classyclix.com/artificial-necklaces/', 'https://www.classyclix.com/artificial-rings/', 'https://www.classyclix.com/artificial-bracelets/', 'https://www.classyclix.com/artificial-bangles/']
        hp= HomePage(driver)
        list_navbar_urls = hp.find_nav_bar_links()
        print("list_navbar_urls:", list_navbar_urls)
        assert set(list_navbar_urls) == set(expected_list_nav_urls)
        self.logger.info(f"Extracted URLs: {list_navbar_urls}")




    def test_verify_top_nav_bar_links_working(self,setup):
        driver = setup
        driver.get("https://www.classyclix.com/")
        driver.maximize_window()
        driver.implicitly_wait(50)
        # expected_list_nav_urls = ['https://www.classyclix.com/artificial-earrings/', 'https://www.classyclix.com/artificial-necklaces/', 'https://www.classyclix.com/artificial-rings/', 'https://www.classyclix.com/artificial-bracelets/', 'https://www.classyclix.com/artificial-bangles/']
        hp= HomePage(driver)
        list_navbar_urls = hp.find_nav_bar_links()
        print("list_navbar_urls:", list_navbar_urls)














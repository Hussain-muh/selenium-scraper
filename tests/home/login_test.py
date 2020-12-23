import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pages.home.login_page import LoginPage
import unittest

class LoginTest(unittest.TestCase):

    def tesr_validLogin(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        baseURL = "https://www.udemy.com/course/bases-de-datos-jairo-galeas/?couponCode=DEJA5ESTRELLAS"
        driverLocation = "/home/hussain/PycharmProjects/selenium/chromedriver"
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver = webdriver.Chrome(driverLocation, options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        login_page = LoginPage(driver)
        login_page("husss", "jass233@gmail.com")

        # loginLink = driver.find_element(By.LINK_TEXT, "Python Scrapy : For Beginners")
        # loginLink.click()

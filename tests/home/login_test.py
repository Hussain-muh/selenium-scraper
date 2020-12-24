import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class LoginTest:

    def tesr_validLogin(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        baseURL = "https://www.real.discount/product-tag/100-off/?s=Python&post_type=product&product_cat=0"
        driverLocation = "/home/hussain/PycharmProjects/selenium/chromedriver"
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver = webdriver.Chrome(driverLocation, options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)
        parentHandle = driver.current_window_handle

        course_list = driver.find_element(By.XPATH,
                                          "//ul[@class='products products-container grid pcols-lg-3 pcols-md-3 "
                                          "pcols-xs-2 pcols-ls-1 pwidth-lg-3 pwidth-md-3 pwidth-xs-2 pwidth-ls-1']")

        course_list.find_element(By.TAG_NAME, "li").click()

        button = driver.find_element(By.XPATH, "//a/button")
        driver.execute_script("arguments[0].click();", button)

        handles = driver.window_handles

        for handle in handles:
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//span[contains(.,'Log in')]").click()
                driver.find_element(By.NAME, "email").send_keys("jass23804@gmail.com")
                driver.find_element(By.NAME, "password").send_keys("plmokn123plm")
                driver.find_element(By.NAME, "submit").click()
                driver.find_element(By.XPATH, "//button[contains(.,'Enroll now')]").click()
                driver.find_element(By.XPATH, "//div[4]/button").click()



LoginTest().tesr_validLogin()

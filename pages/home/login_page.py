import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage():
    _select_python_courses = "/html/body/div[2]/div[2]/header/div[2]/div/div/ul/li[5]/div/div/ul/li[2]/a"
    _order = "orderby"
    _select_cours = "//main[@id='content']/div[4]/ul/li/div/div[2]/a/h3"
    _enrol_link = "/html/body/div[1]/div[3]/div[1]/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[5]/div/button"
    _fullname_input = "id_fullname"
    _email_field = "email--1"
    _password_field = "password"
    _submit_button = "submit-id-submit"
    _enrolnow_button = "Enroll now"

    def getSort(self):
        element = self.driver.find_element(By.CLASS_NAME, self._order)
        sel = Select(element)
        return sel

    def selectCourse(self):
        return self.driver.find_element(By.XPATH, self._select_cours)

    def getEnrolLink(self):
        return self.driver.find_element(By.XPATH, self._enrol_link)

    def getFullnameInput(self):
        return self.driver.find_element(By.ID, self._fullname_input)

    def getEmailInput(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordInput(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getSubmitButton(self):
        return self.driver.find_element(By.ID, self._submit_button)

    def getEnrolNow(self):
        return self.driver.find_element(By.LINK_TEXT, self._enrolnow_button)

    def select_latest(self):
        self.getSort().select_by_value("date")

    def select_course(self):
        self.selectCourse().click()

    def clickEnrolLink(self):
        self.getEnrolLink().click()

    def enterFullname(self, fullname):
        self.getFullnameInput().send_keys(fullname)

    def enterEmail(self, email):
        self.getEmailInput().send_keys(email)

    def enterPassword(self, password):
        return self.getPasswordInput().send_keys(password)

    def clickSubmit(self):
        self.getSubmitButton().click()

    def clickEnrolNow(self):
        self.getEnrolNow().click()

    def _login(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        baseURL = "https://www.real.discount/product-tag/100-off/?s=Python&post_type=product&product_cat=0"
        driverLocation = "/home/hussain/PycharmProjects/selenium/chromedriver"
        os.environ['webdriver.chrome.driver'] = driverLocation
        self.driver = webdriver.Chrome(driverLocation, options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(baseURL)
        self.select_latest()
        self.select_course()
        self.clickEnrolLink()
        self.enterFullname("huss")
        self.enterEmail("jassw@gmail.com")
        self.enterPassword("lkhfvbcyugfbff")
        self.clickSubmit()
        self.clickEnrolNow()


LoginPage()._login()

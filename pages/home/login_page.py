import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():


    _enrol_link = "/html/body/div[1]/div[3]/div[1]/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[5]/div/button"
    _fullname_input = "id_fullname"
    _email_field = "email--1"
    _password_field = "password"
    _submit_button = "submit-id-submit"
    _enrolnow_button = "Enroll now"

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
        baseURL = "https://www.udemy.com/course/bases-de-datos-jairo-galeas/?couponCode=DEJA5ESTRELLAS"
        driverLocation = "/home/hussain/PycharmProjects/selenium/chromedriver"
        os.environ['webdriver.chrome.driver'] = driverLocation
        self.driver = webdriver.Chrome(driverLocation, options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(baseURL)
        self.clickEnrolLink()
        self.enterFullname("huss")
        self.enterEmail("jassw@gmail.com")
        self.enterPassword("lkhfvbcyugfbff")
        self.clickSubmit()
        self.clickEnrolNow()

LoginPage()._login()
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL  =  "https://admin-demo.nopcommerce.com/"
    username = "admin@ourstore.com"
    password = "admin"

    def test_HomePageTitle(self, setup):
        self.driver  = setup
        self.driver.get(self.baseURL)
        act_title =   self.driver.title

        if act_title == "Your Store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            assert False

    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
            self.driver.close()
            assert False

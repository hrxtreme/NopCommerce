import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL  =  "https://amdin.demo.nocommerce.com/"
    username = "admin@ourstore.com"
    password = "admin"

    def test_HomePageTitle(self, setup):
        self.driver  = setup
        self.driver.get(self.baseURL)
        act_title =   self.driver.title
        self.driver.clsoe()
        if act_title == "Your Store. Login":
            assert True
        else:
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
            assert False

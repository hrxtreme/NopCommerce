class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def set_username(self,username):
        self.driver.find.element_by_id(self.textbox_username_id).clear()
        self.driver.find.element_by_id(self.textbox_username_id).send_keys(username)

    def set_password(self,username):
        self.driver.find.element_by_id(self.textbox_password_id_id).clear()
        self.driver.find.element_by_id(self.textbox_password_id_id).send_keys(password)

    def click_login(self):
        self.driver.find.element_by_xpath(self.xpath_login_button).click()

    def click_logout(self):
        self.driver.find.element_by_link_text(self.link_logout_linktext).click()
from pages.locators import BasePageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:

    login_form = (By.CSS_SELECTOR, "#login_form")
    email_login_form = (By.CSS_SELECTOR, "#id_login-username")
    pass_login_form = (By.CSS_SELECTOR, "#id_login-password")
    submit_login_button = (By.CSS_SELECTOR, "[name='login_submit']")

    register_form = (By.CSS_SELECTOR, "#register_form")
    email_register_form = (By.CSS_SELECTOR, "#id_registration-email")
    pass_register_form = (By.CSS_SELECTOR, "#id_registration-password1")
    repeat_pass_register_form = (By.CSS_SELECTOR, "#id_registration-password2")
    submit_register_button = (By.CSS_SELECTOR, "[name='registration_submit']")

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"
        
    def register_new_user(self, email, password):
        self.go_to_login_page_for_reg()
        login_field = self.find_element(LoginPageLocators.email_register_form)
        password_field = self.find_element(LoginPageLocators.pass_register_form)
        rep_password_field = self.find_element(LoginPageLocators.repeat_pass_register_form)
        login_field.send_keys(email)
        password_field.send_keys(password)
        rep_password_field.send_keys(password)
        self.find_element(LoginPageLocators.submit_register_button).click()
        return self.should_be_authorized_user()
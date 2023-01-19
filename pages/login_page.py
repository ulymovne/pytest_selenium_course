from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        cur_element = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        cur_element.send_keys(email)
        cur_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        cur_element.send_keys(password)
        cur_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        cur_element.send_keys(password)
        cur_element = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        cur_element.click()
        self.browser.implicitly_wait(4)

    def should_be_user_authorized(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login from is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register from is not presented"
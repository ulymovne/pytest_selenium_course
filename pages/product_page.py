from .base_page import BasePage
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def should_be_guest_add_to_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET_FORM), "Add to basket form is not presented"

    def add_product_to_basket(self):
        login_link = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_FORM)
        login_link.click()
        #self.solve_quiz_and_get_code()

    def should_be_guest_message_cost_basket(self, product_price):
        cost_basket = self.browser.find_element(*BasketPageLocators.COST_BASKET).text
        assert  product_price == cost_basket, \
            f'Price_product ({product_price}) is not equal to cost of basket ({cost_basket})'

    def should_be_guest_message_product_name_add(self, product_name):
        product_message = self.browser.find_element(*BasketPageLocators.PRODUCT_MESSAGE).text
        assert product_name == product_message, \
            f'Product ({product_name}) is not in message to add in basket ({product_message})'

    def get_product_name(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
    def get_product_price(self):
        return  self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def should_be_disappear_message(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Message is not disappear, but should be"
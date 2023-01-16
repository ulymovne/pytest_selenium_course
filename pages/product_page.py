from .base_page import BasePage
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def should_be_guest_add_to_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET_FORM), "Add to basket form is not presented"

    def add_product_to_basket(self):
        login_link = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_FORM)
        login_link.click()
        self.solve_quiz_and_get_code()

    def should_be_guest_message_cost_basket(self):
        cost_basket = self.browser.find_element(*BasketPageLocators.COST_BASKET).text
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        assert  product_price == cost_basket, f'Price_product ({product_price}) is not equal to cost of basket ({cost_basket})'

    def should_be_guest_message_product_name_add(self):
        product_message = self.browser.find_element(*BasketPageLocators.PRODUCT_MESSAGE).text
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        assert product_name == product_message, f'Product ({product_name}) is not in message to add in basket ({product_message})'
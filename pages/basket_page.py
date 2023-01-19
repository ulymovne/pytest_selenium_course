from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_guest_product_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def should_be_guest_empty_basket(self):
        basket_text_empty = self.browser.find_element(*BasketPageLocators.BASKET_TEXT_EMPTY).text
        assert basket_text_empty == 'Your basket is empty. Continue shopping', \
            f"Text '{basket_text_empty}' not is 'Your basket is empty. Continue shopping'."
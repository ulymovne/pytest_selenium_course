from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest
LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.email = 'igor' + str(time.time()) + '@fakemail.org'
        self.password = 'fakepass' + str(time.time())
        page = LoginPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        page.register_new_user(self.email, self.password)
        page.should_be_user_authorized()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_be_guest_add_to_basket_form()
        page.add_product_to_basket()
        page.should_be_guest_message_cost_basket(page.get_product_price())
        page.should_be_guest_message_product_name_add(page.get_product_name())
        page.should_not_be_success_message()
        page.should_be_disappear_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_guest_add_to_basket_form()
    page.add_product_to_basket()
    page.should_be_guest_message_cost_basket(page.get_product_price())
    page.should_be_guest_message_product_name_add(page.get_product_name())
    page.should_not_be_success_message()
    page.should_be_disappear_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappear_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link=LINK):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_guest_product_basket()
    page.should_be_guest_empty_basket()
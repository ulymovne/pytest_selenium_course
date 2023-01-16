from .pages.product_page import ProductPage
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_guest_add_to_basket_form()
    page.add_product_to_basket()
    page.should_be_guest_message_cost_basket(page.get_product_price())
    page.should_be_guest_message_product_name_add(page.get_product_name())


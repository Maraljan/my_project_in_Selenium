from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    product = ProductPage(browser, link)
    product.open()
    product.add_basket()
    product.check_message()
    product.check_price()

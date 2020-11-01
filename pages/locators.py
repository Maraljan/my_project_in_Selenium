from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    TITLE = (By.CSS_SELECTOR, ".product_main  > h1")
    TITLE1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE = (By.CSS_SELECTOR, ".in > div > p:nth-child(1) > strong")
    PRICE1 = (By.CSS_SELECTOR, ".product_main > p.price_color")

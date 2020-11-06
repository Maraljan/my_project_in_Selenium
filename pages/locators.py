from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    TITLE = (By.CSS_SELECTOR, ".product_main  > h1")
    TITLE1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRICE = (By.CSS_SELECTOR, ".in > div > p:nth-child(1) > strong")
    PRICE1 = (By.CSS_SELECTOR, ".product_main > p.price_color")


class BasketPageLocators:
    BASKET_TO_CLICK = (By.CSS_SELECTOR, ".hidden-xs > span > a")
    EMPTY_PRODUCT = (By.CSS_SELECTOR, ".hidden-xs > div")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")


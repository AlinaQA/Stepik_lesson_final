from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    view_basket = (By.CSS_SELECTOR, ".btn-group > [href='/en-gb/basket/']")

class BasketPageLocators:

    empty_basket = (By.CSS_SELECTOR, ".basket-items")
    empty_text_basket = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators():
    pass

class ProductPageLocators:
    
    book_name = (By.CSS_SELECTOR, ".product_main > h1")
    price = (By.CSS_SELECTOR, ".product_main > .price_color")
    add_to_basket_button = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    book_name_message = (By.CSS_SELECTOR, ".alertinner > strong")
    price_message = (By.CSS_SELECTOR, ".alertinner > p > strong")
    success_mesage = (By.CSS_SELECTOR, ".alert-success")


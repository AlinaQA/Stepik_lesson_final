from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
        
    def value_price(self):
        return self.find_element(ProductPageLocators.add_to_basket_button).text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_basket_button), "'Add to basket' button is not presented"

    def click_add_to_basket_button(self):
        return self.find_element(ProductPageLocators.add_to_basket_button).click()

    def should_be_name_book_in_message(self):
        name_book = self.find_element(ProductPageLocators.book_name).text
        print(name_book)
        name_book_message = self.find_element(ProductPageLocators.book_name_message).text
        print(name_book_message)
        assert name_book == name_book_message, "Book's name in message is wrong"

    def should_be_value_price_in_message(self):
        value_price = self.find_element(ProductPageLocators.price).text
        print(value_price)
        value_price_message = self.find_element(ProductPageLocators.price_message).text
        print(value_price_message)
        assert value_price == value_price_message, "Basket's price in message is wrong"

    def add_book_to_basket(self):
        ProductPage.should_be_add_to_basket_button(self)
        ProductPage.click_add_to_basket_button(self)
        ProductPage.solve_quiz_and_get_code(self)
        ProductPage.should_be_name_book_in_message(self)
        ProductPage.should_be_value_price_in_message(self)

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.success_mesage), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.success_mesage), \
                "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.success_mesage), \
                "Success message is presented, but should not be"

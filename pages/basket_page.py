from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.empty_basket), "Basket is not empty, but should be"

    def should_be_empty_text_basket(self):
        empty_text = self.find_element(BasketPageLocators.empty_text_basket).text
        assert empty_text == "Your basket is empty. Continue shopping", "Basket is not empty"
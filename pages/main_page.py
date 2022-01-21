from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import *
from .login_page import LoginPage

class MainPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
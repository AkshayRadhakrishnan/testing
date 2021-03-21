from config.config1 import *
from Library.web_utils import WebUtils
from Library.file_library import Readfile

r = Readfile()
w = WebUtils()
element, keys = r.read_object(filepath)

class Shopping:

    def __init__(self, driver):
        self.driver = driver
    def computer(self):
        w.mouse_move(self.driver, element["computer"])
    def desktop(self):
        w.mouse_click(self.driver, element["desktop"])
    def desktop_new(self):
        w.click_method(self.driver, element["desktop_new"])
    def add_to_cart(self):
        w.click_method(self.driver, element["add_to_cart"])
    def select_one_option(self):
        w.click_method(self.driver, element["select_one_option"])
    def add_to_cart_again(self):
        w.click_method(self.driver, element["add_to_cart_again"])
    def shopping_cart(self):
        w.click_method(self.driver, element["shopping_cart"])
    def continue_shopping(self):
        w.click_method(self.driver, element["continue_shopping"])
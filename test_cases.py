from Page.shopping import Shopping
from Library.base_fixtures import *
from time import sleep


class TestSnap(DriverInit):


    def test_shoping(self):
        obj = Shopping(self.driver)
        obj.computer()
        sleep(3)
        obj.desktop()
        sleep(3)
        obj.desktop_new()
        sleep(3)
        obj.add_to_cart()
        sleep(3)
        obj.select_one_option()
        sleep(3)
        obj.add_to_cart_again()
        sleep(3)
        obj.shopping_cart()
        sleep(3)
        #obj.continue_shopping()


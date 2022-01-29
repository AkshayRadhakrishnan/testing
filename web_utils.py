from selenium.webdriver.common.action_chains import ActionChains


class WebUtils:

    @staticmethod
    def click_method(driver, element):
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).click()

    @staticmethod
    def mouse_move(driver, element):
        action = ActionChains(driver)
        loc_type, loc_value = element
        ele = driver.find_element(loc_type, loc_value)
        action.move_to_element(ele).perform()

    @staticmethod
    def mouse_click(driver, element):
        action = ActionChains(driver)
        loc_type, loc_value = element
        ele = driver.find_element(loc_type, loc_value)
        action.move_to_element(ele).click().perform()


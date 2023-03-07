from locators.elements_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def check_world_file(self):
        self.element_is_visible(self.locators.HOME_BUTTON).click()
        self.element_is_visible(self.locators.DOWNLOADS_BUTTON).click()
        self.element_is_visible(self.locators.WORLD_FILE).click()
        result = self.element_is_present(self.locators.RESULT).text
        return result


from .PageBase import BasePage
from SectionBase import SectionBase
from .locators import SectionHeaderLocators
from lib.checks import CHECK

class SectionHeader(SectionBase):

    def __init__(self):
        super().__init__(SectionHeaderLocators.array)

#region NAVIGATION

    def go_to_login_page(self):
        element = self.browser.find_element(*SectionHeaderLocators.LINK_LOGIN)
        element.click()

    def go_to_rent_page(self):
        element = self.browser.find_element(*SectionHeaderLocators.LINK_RENT)
        element.click()
        # return BasketPage(browser=self.browser,
        #                   url=self.browser.current_url)  # возвращаем объект basketpage если он нужен

    def go_to_lend_page(self):
        element = self.browser.find_element(*SectionHeaderLocators.LINK_LEND)
        element.click()        

#endregion NAVIGATION


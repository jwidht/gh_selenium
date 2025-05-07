# from .locators import LoginPageLocators
from .PageBase import BasePage
from ..settings import BASE_URL
from ..pages.locators import PageEntryLocators,SectionHeaderLocators,PageLoginLocators,PageRentLocators

class PageRent(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url
                         , url_token = "rent"
                         , locator_list = SectionHeaderLocators.list + PageRentLocators.list 
                         )
        
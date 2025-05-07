
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
# from .locators import PageBaseLocators
from ..lib.checks import CHECK

class BasePage():

    def __init__(self, browser, url, url_token = None, locator_list = None):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout), timeout=10

        # for checks:
        self.url_token = url_token
        self.locator_list = locator_list
        
    def open(self): 
        self.browser.get(self.url)
    
    def run_checks(self):
        #run_presence_checks()
        if self.url_token is not None: 
            CHECK.in_url(self.browser, self.url_token)
        if self.locator_list != None:
            CHECK.elements_present(self.browser, self.locator_list)

#region ELEMENT PRESENCE
    # def should_be_login_link(self):
    #     assert self.is_element_present(*PageBaseLocators.LINK_LOGIN), "Login link is not presented"

    # def should_be_rent_link(self):
    #     assert self.is_element_present(*PageBaseLocators.LINK_RENT), "User icon is not presented," \
    #                                                              " probably unauthorised user"
#endregion ELEMENT PRESENCE





    # def solve_quiz_and_get_code(self):
    #     alert = self.browser.switch_to.alert
    #     x = alert.text.split(" ")[2]
    #     answer = str(math.log(abs((12 * math.sin(float(x))))))
    #     alert.send_keys(answer)
    #     alert.accept()
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Your code: {alert_text}")
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No second alert presented")

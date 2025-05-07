from selenium.webdriver.common.by import By

class Locator():
    def __init__(self,name,how):
        self.name = name
        self.how = how

class SectionHeaderLocators():
    # <a href="/login">Вход</a>
    LINK_LOGIN = Locator("LINK_LOGIN" , (By.CSS_SELECTOR, "a[href='/login']")  )
    LINK_LEND =  Locator("LINK_LEND"  , (By.CSS_SELECTOR, "a[href='/lend']")   )
    LINK_RENT =  Locator("LINK_RENT"  , (By.CSS_SELECTOR, "a[href='/rent']")   )

    list = [LINK_LOGIN, LINK_LEND, LINK_RENT]

class PageEntryLocators():
    BTN_BEGIN = Locator("BTN_BEGIN" ,(By.CSS_SELECTOR, "div.mx-auto > button.btn1") )
    BTN_SUBSCRIBE = Locator("BTN_SUBSCRIBE" ,(By.CSS_SELECTOR, "form > button.btn1") )
    TEXT_EMAIL = Locator("TEXT_EMAIL" ,(By.CSS_SELECTOR, "form > input[name='email']") )
    SELECT_LANG = Locator("SELECT_LANG" ,(By.CSS_SELECTOR, "select[name='PrefUICulture']") )
    FLAG_LANG = Locator("FLAG_LANG" ,(By.CSS_SELECTOR, "div > img.cursor-pointer[width='20px']") )

    # <div><img width="20px" class="mx-4 cursor-pointer" title="ru-RU" src="/flags/ru.svg" alt="ru-RU"></div>
    #LOGIN_LINK = (By.ID, "#registration_link")
    list = [ BTN_BEGIN, BTN_SUBSCRIBE , TEXT_EMAIL, SELECT_LANG, FLAG_LANG]

class PageLoginLocators():
    TEXT_EMAIL = Locator("TEXT_EMAIL" ,(By.CSS_SELECTOR, "input[name='email']") )
    TEXT_PWD = Locator("TEXT_PWD"     ,(By.CSS_SELECTOR, "input[name='password']") )
    BTN_LOGIN = Locator("BTN_LOGIN"   ,(By.CSS_SELECTOR, "div.mx-auto > button.btn1") )

    list = [TEXT_EMAIL, TEXT_PWD, BTN_LOGIN]
    # LOGIN_LINK = (By.ID, "id_login-username")
    # PWD_LINK = (By.ID, "id_login-password") 
    # REG_EMAIL_LINK = (By.ID, "id_registration-email")
    # REG_PWD_LINK = (By.ID, "id_registration-password1") 
    # REG_PWD2_LINK = (By.ID, "id_registration-password2") 
    # REG_BUTTON = (By.NAME, "registration_submit")

class PageRentLocators():
    TB_LOCATION = Locator("TB_LOCATION" , (By.ID, "default-search") )
    BTN_GO = Locator("BTN_GO"   ,(By.CSS_SELECTOR, "div > button.btn1.btn-clr") )
    list = [TB_LOCATION, BTN_GO]
#     BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
#     H1_TITLE = (By.CSS_SELECTOR, "h1")
#     P_PRICE = (By.CSS_SELECTOR, "p.price_color")
#     ALERT_INNER = (By.CSS_SELECTOR, "div.alertinner > strong")
#     SUCCESS_MESSAGE= (By.CSS_SELECTOR, "div.alert-success")
#     P_TOTAL = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    # PWD_LINK = (By.ID, "id_login-password") 
    # REG_EMAIL_LINK = (By.ID, "id_registration-email")
    # REG_PWD_LINK = (By.ID, "id_registration-password1") 
    # REG_PWD2_LINK = (By.ID, "id_registration-password2") 

# class BasketPageLocators():
#     BTN_GO_TO_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
#     # <div id="content_inner"> <p> Your basket is empty.<a href="/en-gb/">Continue shopping</a> </p></div>
#     EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p ")
#     BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
 
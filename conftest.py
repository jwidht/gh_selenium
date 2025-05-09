import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .lib.common import printh,printhe

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', #None, #'en',
                     help="Choose language: en, ru, etc")
                    
@pytest.fixture(scope="function")
def browser(request):
    printh("FUNCTION FIXTURE START")
    user_language = request.config.getoption("language")
    print(f"Starting browser with user_language={user_language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10) # 10s wait for elements
    yield browser
    print("\nquit browser...")
    browser.quit()
    printhe("FUNCTION FIXTURE END")
   
    

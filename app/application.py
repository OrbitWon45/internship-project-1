from pages.signin_page import SigninPage
from pages.off_plan_page import OffPlanPage
from pages.settings_page import SettingsPage
from pages.support_page import SupportPage
from pages.news_page import NewsPage

class Application:

    def __init__(self, driver):
        self.signin_page = SigninPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.settings_page = SettingsPage(driver)
        self.support_page = SupportPage(driver)
        self.news_page = NewsPage(driver)



        
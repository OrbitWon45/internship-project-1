from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class NewsPage(Page):

    VIEW_IN_TELEGRM_BTN = (By.CSS_SELECTOR, 'a.tgme_action_button_new.shine')

    def verify_news_page_opens(self):
        self.wait_for_element_to_appear(*self.VIEW_IN_TELEGRM_BTN)

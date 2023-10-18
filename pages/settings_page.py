from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SettingsPage(Page):
    SUPPORT_BTN = (By.CSS_SELECTOR, 'a[href*="https://wa.me/message"] div.setting-text')
    NEWS_BTN = (By.CSS_SELECTOR, 'a[href="https://t.me/reellydxb"] div.setting-text')

    def click_on_support(self):
        self.wait_for_element_clickable_click(*self.SUPPORT_BTN)

    def click_on_news_option(self):
        self.wait_for_element_clickable_click(*self.NEWS_BTN)





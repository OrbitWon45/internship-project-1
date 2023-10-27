from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class SettingsPage(Page):
    SUPPORT_BTN = (By.CSS_SELECTOR, 'a[href*="https://wa.me/message"] div.setting-text')
    NEWS_BTN = (By.CSS_SELECTOR, 'a[href="https://t.me/reellydxb"] div.setting-text')

    def click_on_support(self):
        self.wait_for_element_clickable_click(*self.SUPPORT_BTN)

    def click_on_news_option(self):
        self.wait_for_element_clickable_click(*self.NEWS_BTN)

    def click_on_news_option_mobile(self):
        news_btn = (By.CSS_SELECTOR, 'a[href="https://t.me/reellydxb"] div.setting-text')
        self.wait.until(EC.presence_of_element_located(news_btn))
        self.wait_for_element_clickable_click(*self.NEWS_BTN)






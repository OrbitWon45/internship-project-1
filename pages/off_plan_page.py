from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class OffPlanPage(Page):

    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a[href="/settings"] div.menu-button-text')


    def click_on_settings(self):
        self.wait_for_element_clickable_click(*self.SETTINGS_BUTTON)


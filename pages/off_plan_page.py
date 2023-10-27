from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class OffPlanPage(Page):

    SETTINGS_BTN = (By.XPATH, '//a[@href="/settings"]//div[@class="menu-icon w-embed"]')
    MOBILE_MENU_BTN = (By.CSS_SELECTOR, 'a.menu-button-wrapper.w-inline-block')

    def open_off_plan_page(self):
        self.open_url()
        #sleep(5)

    def click_on_settings(self):
        self.wait_for_element_clickable_click(*self.SETTINGS_BTN)

    def click_on_menu_mobile(self):
        self.wait_for_element_clickable_click(*self.MOBILE_MENU_BTN)


